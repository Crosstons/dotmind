import google.generativeai as genai
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from db_json import chat_history_manager, private_key_manager, address_book
from datetime import datetime
import requests
import asyncio

genai.configure(api_key="AIzaSyAbM0fgCccbiHCPw0M56RF69GLhEw9JZoM")

# Set up the model
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

async def balance_check(input):
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

async def create_key(input):
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

async def delete_key(input):
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
    return f'deleted keypair for \"{alias}\"'