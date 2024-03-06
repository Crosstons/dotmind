import json
import os

def create_private_key_manager_file(filename):
    try:
        with open(filename, "w") as f:
            json.dump([], f)
    except IOError as e:
        print("Error creating file:", e)

def load_private_key_manager_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return []

def save_private_key_manager_data(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print("Error saving data:", e)

def add_private_key_object(filename, alias, private_key):
    data = load_private_key_manager_data(filename)
    new_object = {"alias": alias, "private_key": private_key}
    data.append(new_object)
    save_private_key_manager_data(filename, data)

def update_private_key_object(filename, alias, new_private_key):
    data = load_private_key_manager_data(filename)
    for obj in data:
        if obj["alias"] == alias:
            obj["private_key"] = new_private_key
            break
    save_private_key_manager_data(filename, data)

def delete_private_key_object(filename, alias):
    data = load_private_key_manager_data(filename)
    data = [obj for obj in data if obj["alias"] != alias]
    save_private_key_manager_data(filename, data)

def get_private_key_from_alias(filename, alias):
    data = load_private_key_manager_data(filename)
    for obj in data:
        if obj["alias"] == alias:
            return obj["private_key"]
    return None


# ============= Test ===============

filename = './backend/db_json/private_key_manager.json'

try:
    create_private_key_manager_file(filename)

    add_private_key_object(filename, "Binance Private Key", "/home/user/desktop/")
    add_private_key_object(filename, "Coinbase Private Key", "key2")

    print(load_private_key_manager_data(filename))

    print(get_private_key_from_alias(filename, "Binance Private Key"))
    print(get_private_key_from_alias(filename, "Coinbase Private Key"))
except Exception as e:
    print("An error occurred:", e)
