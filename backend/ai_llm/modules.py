import google.generativeai as genai
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from db_json import chat_history_manager
from datetime import datetime
import requests
import asyncio

genai.configure(api_key="AIzaSyAwyyY0j-y3_iiJ3UXVWlIqvbi8PMB9u74")

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

def balance_check(input):
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

    convo.send_message("Only give the url of the network - what is the balance of Bholu on Aleph Zero Testnet Network?")
    print(convo.last.text)

    convo.send_message("Only give the url of the network - what is the balance of Bholu on Aleph Zero Testnet Network?")
    print(convo.last.text)

    substrate = SubstrateInterface(convo.last.text)

    result = substrate.query('System', 'Account', ['5HMrodMT8vphQUyd3PxKE7i6G4rPLEqeZG18ener4Mvet1ei'])
    print(result.value['data'])