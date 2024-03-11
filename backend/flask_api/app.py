from flask import Flask, jsonify, request 
from db_json import chat_history_manager, private_key_manager, address_book, transfer_manager
from ai_llm.query import process_query

app = Flask("DotMind") 

def run_app():
    app.run(debug=True)

@app.route('/chat_history/', methods=['GET']) 
def history(): 
    # Load chat history data
    chat_history_data = chat_history_manager.get_chat_history()
    response = jsonify(chat_history_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
@app.route('/addr_book/', methods=['GET']) 
def address_book(): 
    # Load chat history data
    addr_book_data = address_book.load_address_book_data()
    response = jsonify(addr_book_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 

@app.route('/scheduled_transfers/', methods=['GET']) 
def address_book(): 
    # Load chat history data
    scheduled = transfer_manager.load_transfer_manager_data()
    response = jsonify(scheduled)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 

@app.route('/address/<key>', methods=['GET'])
def get_key(key):
    addr = address_book.get_value_from_key(key)
    return jsonify(addr)

@app.route('/prompt/', methods=['POST'])
async def prompt():
    user_prompt = request.get_json()
    print(user_prompt)
    out = await process_query(user_prompt['prompt'])

    # Validate the data and create the user (implementation omitted)
    return jsonify(out)
