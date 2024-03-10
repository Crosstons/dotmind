import google.generativeai as genai
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from db_json import chat_history_manager, private_key_manager, address_book, transfer_manager
from datetime import datetime
import requests
import asyncio
import re


def extract_single_quoted(text):
    pattern = r"'(?P<content>.*?)'"  # Named capture group
    return [match.group("content") for match in re.finditer(pattern, text)]

def read_pk(path):
    try:
        with open(path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:  # Catch other potential errors
        print(f"An error occurred: {e}")
        return None

# Set up the model

# replace the "KEY" with your own Google Gemini API key
genai.configure(api_key="KEY")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# safety settings
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

async def price_check(input):
    try:
        convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["Here's a sample url of a coinbase API which fetches the price information of Bitcoin-USD pair (https://api.coinbase.com/v2/prices/BTC-USD/spot), I will next provide you a name of a cryptocurrency with its symbol or only a name, I want you to find the corresponding symbol for and construct the URL for its price feed on coinbase. The output that I expect is only URL and no extra text or information."]
        },
        {
            "role": "model",
            "parts": ["​"]
        },
        ])

        convo.send_message(input)
        print(convo.last.text)

        response = requests.get(convo.last.text)
        temp = response.json()
        print(temp["data"]["amount"])
        curr = datetime.now()
        chat_history_manager.add_chat_entry(input, temp["data"]["amount"], str(curr.now()))
        return response.json()
    except:
        return "Something went wrong, please try again"

async def balance_check(input):
    try:
        convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["Here's a sample url of a dwellir API endpoint which connects with a node of Aleph Zero network and enables us to make requests to the network - wss://aleph-zero-rpc.dwellir.com, for testnet the url becomes - wss://aleph-zero-testnet-rpc.dwellir.com, I will next provide you a prompt containing name of some other Polkadot ecosystem chain, I want you to only build the corresponding dwellir wss api for it. The output should be only the URL, do not give extra text or information."]
        },
        {
            "role": "model",
            "parts": ["​"]
        },
        ])

        convo.send_message(f"Only give the url of the network - {input}")
        url = convo.last.text
        print(url)

        # Identify the alias and get it from the address book -

        convo.send_message(f"Identify the alias or name given in the string and only return it as the response (no other information should be present in the response) - {input}")
        alias = convo.last.text
        print(alias)
        addr = address_book.get_value_from_key(alias)
        print(addr)

        substrate = SubstrateInterface(url)

        result = substrate.query('System', 'Account', [addr])
        print(result.value['data'])

        # updating dbs
        curr = datetime.now()
        chat_history_manager.add_chat_entry(input, f'This is the raw balance of the address - {result.value['data']['free']}, please adjust for the decimals', str(curr.now()))

        return result.value['data']
    except:
        return "something went wrong, please try again"

async def create_key(input):
    try:
        convo = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["Identify the alias or name given in the string and only return it as the response (no other information should be present in the response)"]
            },
            {
                "role": "model",
                "parts": ["​"]
            },
        ])

        # finding out the alias used in the prompt

        convo.send_message(input)
        alias = convo.last.text
        print(alias)

        # creating a keypair and writing it to a file

        new_key = Keypair.generate_mnemonic()
        print(new_key)
        with open(f'./ai_llm/local_keys/{alias}.txt', 'w') as file:  
            file.write(new_key)
        addr = Keypair.create_from_mnemonic(new_key)
        print(addr)

        # updating dbs

        curr = datetime.now()
        chat_history_manager.add_chat_entry(input, f'Keypair created and stored in file - ./ai_llm/local_keys/{alias}.txt', str(curr.now()))
        private_key_manager.add_private_key_object(alias, f'./ai_llm/local_keys/{alias}.txt')

        return f'./ai_llm/local_keys/{alias}.txt'
    except:
        return "something went wrong, please try again"

async def delete_key(input):
    try:
        convo = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["Identify the alias or name given in the string and only return it as the response (no other information should be present in the response)"]
            },
            {
                "role": "model",
                "parts": ["​"]
            },
        ])

        # finding out the alias used in the prompt

        convo.send_message(input)
        alias = convo.last.text
        print(alias)

        # updating dbs

        curr = datetime.now()
        if private_key_manager.delete_private_key_object(alias) == True:
            chat_history_manager.add_chat_entry(input, f'Keypair file deleted - ./ai_llm/local_keys/{alias}.txt', str(curr.now()))
        else:
            return "Alias does not exist or something else went wrong :("
        return f'deleted keypair for "{alias}"'
    except:
        return "something went wrong, please try again"

async def address_add(input):
    try:
        _temp = input
        addr = extract_single_quoted(input)[0]
        input = input.replace(f"'{addr}'", "")

        convo = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["Identify the alias or name given in the string and only return it as the response (no other information should be present in the response)"]
            },
            {
                "role": "model",
                "parts": ["​"]
            },
        ])

        # finding out the alias used in the prompt

        convo.send_message(input)
        alias = convo.last.text
        print(alias)

        # updating dbs

        curr = datetime.now()
        if address_book.add_json_object(alias, addr) == True:
            chat_history_manager.add_chat_entry(_temp, f"alias '{alias}' added for the address - '{addr}'", str(curr.now()))
        else:
            return "Alias already exists, try deleting and adding again or something else went wrong :("
        return f'Alias "{alias}" added to the address book'
    except:
        return "something went wrong, please try again"
    
async def address_remove(input):
    try:
        addr = extract_single_quoted(input)
        _temp = input
        input = input.replace(f"'{addr}'", "")

        convo = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["Identify the alias or name given in the string and only return it as the response (no other information should be present in the response)"]
            },
            {
                "role": "model",
                "parts": ["​"]
            },
        ])

        # finding out the alias used in the prompt

        convo.send_message(input)
        alias = convo.last.text
        print(alias)

        # updating dbs

        curr = datetime.now()
        if address_book.delete_json_object(alias) == True:
            chat_history_manager.add_chat_entry(_temp, f'alias {alias} deleted from the address book', str(curr.now()))
        else:
            return "Alias doesn't exist or something else went wrong :("
        return f'Alias "{alias}" deleted from the address book'
    except:
        return "something went wrong, please try again"
    
async def instant_transfer(input):
    try:
        convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["Here's a sample url of a dwellir API endpoint which connects with a node of Aleph Zero network and enables us to make requests to the network - wss://aleph-zero-rpc.dwellir.com, for testnet the url becomes - wss://aleph-zero-testnet-rpc.dwellir.com, I will next provide you a prompt containing name of some other Polkadot ecosystem chain, I want you to only build the corresponding dwellir wss api for it. The output should be only the URL, do not give extra text or information."]
        },
        {
            "role": "model",
            "parts": ["​"]
        },
        ])

        convo.send_message(f"Only give the dwellir wss url for the network being mentioned - {input}")
        url = convo.last.text
        print(url)

        convo.send_message(f"You are being given a transaction prompt, from which you need to find out the amount that the user wants to send. Only give amount as output (for example - 10) - {input}")
        amt = convo.last.text
        print(amt)

        convo.send_message(f"Identify the alias or name given in the string and only return it as the response (no other information should be present in the response) - {input}")
        alias = convo.last.text
        print(alias)

        substrate = SubstrateInterface(url)

        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer_allow_death',
            call_params={
                'dest': address_book.get_value_from_key(alias),
                'value': amt
            }
        )

        seed = read_pk(private_key_manager.get_private_key_from_alias("default"))

        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=Keypair.create_from_mnemonic(seed))

        try:
            receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)

            print('Extrinsic "{}" included in block "{}"'.format(
                receipt.extrinsic_hash, receipt.block_hash
            ))

            if receipt.is_success:

                print('✅ Success, triggered events:')
                for event in receipt.triggered_events:
                    print(f'* {event.value}')

                # updating dbs

                curr = datetime.now()
                chat_history_manager.add_chat_entry(input, f'transfer executed successfully for {amt} to {alias} using the rpc {url}', str(curr.now()))
                
                return "transfer instruction was successfull"

            else:
                print('⚠️ Extrinsic Failed: ', receipt.error_message)

        except SubstrateRequestException as e:
            print("Failed to send: {}".format(e))

            curr = datetime.now()
            chat_history_manager.add_chat_entry(input, f'transfer execution failed due to the error - {e}', str(curr.now()))
    
    except:
        return "failed to send the transaction, something went wrong"

async def timed_transfer(input):
    try:
        convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["Here's a sample url of a dwellir API endpoint which connects with a node of Aleph Zero network and enables us to make requests to the network - wss://aleph-zero-rpc.dwellir.com, for testnet the url becomes - wss://aleph-zero-testnet-rpc.dwellir.com, I will next provide you a prompt containing name of some other Polkadot ecosystem chain, I want you to only build the corresponding dwellir wss api for it. The output should be only the URL, do not give extra text or information."]
        },
        {
            "role": "model",
            "parts": ["​"]
        },
        ])

        convo.send_message(f"Only give the dwellir wss url for the network being mentioned - {input}")
        url = convo.last.text
        print(url)

        convo.send_message(f"You are being given a transaction prompt, from which you need to find out the amount that the user wants to send. Only give amount as output (for example - 10) - {input}")
        amt = convo.last.text
        print(amt)

        convo.send_message(f"Identify the alias or name given in the string and only return it as the response (no other information should be present in the response) - {input}")
        alias = convo.last.text
        print(alias)

        curr = datetime.now()
        convo.send_message(f"The current date time is {str(curr)}. I will give you a prompt which will have a target time in it, i want you to give me the target datetime relative to the current time and the response should only contain the output datetime - {input}")
        _timed = convo.last.text
        print(_timed)

        transfer_manager.schedule_transfer("default", alias, amt, _timed, url)
        chat_history_manager.add_chat_entry(input, f'scheduled transfer : {amt} to {alias} on {_timed} on {url}', str(curr.now()))

        return "Scheduled transfer successfully"
    
    except:
        return "something went wrong while scheduling transfer"