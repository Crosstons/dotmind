from flask import Flask, jsonify, request 
from db_json import chat_history_manager, private_key_manager, address_book, transfer_manager

app = Flask("DotMind") 

def run_app():
    app.run(debug=True)

@app.route('/chat_history/', methods=['GET']) 
def history(): 
    # Load chat history data
    chat_history_data = chat_history_manager.get_chat_history()
    return jsonify(chat_history_data)

@app.route('/address/<key>', methods=['GET'])
def show_article(key):
    addr = address_book.get_value_from_key(key)
    return jsonify(addr)

@app.route('/prompt/', methods=['POST'])
def create_user():
    user_prompt = request.get_json()
    print(user_prompt)

    # Validate the data and create the user (implementation omitted)
    return jsonify(user_prompt)