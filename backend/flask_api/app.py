from flask import Flask, jsonify, request 
from db_json import private_key_manager

app = Flask("DotMind") 

def run_app():
    app.run(debug=True)

@app.route('/history', methods=['GET']) 
def history(): 
    # Load chat history data
    chat_history_data = private_key_manager.load_private_key_manager_data()
    return jsonify(chat_history_data)