import json
import os

FILENAME = './db_json/json_files/chat_history.json'

def load_chat_history_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return []

def save_chat_history_data(data):
    try:
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print("Error saving data:", e)

def add_chat_entry(prompt, response, timestamp):
    data = load_chat_history_data()
    new_entry = {"prompt": prompt, "response": response, "timestamp": timestamp}
    data.append(new_entry)
    save_chat_history_data(data)

def get_chat_history():
    return load_chat_history_data()


# ============= Test ===============

try:

    add_chat_entry("How are you?", "I'm fine, thank you!", "2024-03-10 08:00:00")
    add_chat_entry("What's the weather like today?", "It's sunny and warm.", "2024-03-10 08:05:00")

    print(get_chat_history())
except Exception as e:
    print("An error occurred:", e)