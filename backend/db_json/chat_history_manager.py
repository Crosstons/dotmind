import json
import os

def create_chat_history_file(filename):
    try:
        with open(filename, "w") as f:
            json.dump([], f)
    except IOError as e:
        print("Error creating file:", e)

def load_chat_history_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return []

def save_chat_history_data(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print("Error saving data:", e)

def add_chat_entry(filename, prompt, response, timestamp):
    data = load_chat_history_data(filename)
    new_entry = {"prompt": prompt, "response": response, "timestamp": timestamp}
    data.append(new_entry)
    save_chat_history_data(filename, data)

def get_chat_history(filename):
    return load_chat_history_data(filename)


# ============= Test ===============

filename = 'chat_history.json'

try:
    create_chat_history_file(filename)

    add_chat_entry(filename, "How are you?", "I'm fine, thank you!", "2024-03-10 08:00:00")
    add_chat_entry(filename, "What's the weather like today?", "It's sunny and warm.", "2024-03-10 08:05:00")

    print(get_chat_history(filename))
except Exception as e:
    print("An error occurred:", e)