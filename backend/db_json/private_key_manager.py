import json
import os

FILENAME = './db_json/json_files/private_key_manager.json'

def load_private_key_manager_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return []

def save_private_key_manager_data(data):
    try:
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print("Error saving data:", e)

def add_private_key_object(alias, private_key):
    data = load_private_key_manager_data()
    if not any(obj["alias"] == alias for obj in data):
        new_object = {"alias": alias, "private_key": private_key}
        data.append(new_object)
        save_private_key_manager_data(data)
        return True
    else:
        print("Alias already exists.")
        return False

def update_private_key_object(alias, new_private_key):
    data = load_private_key_manager_data()
    for obj in data:
        if obj["alias"] == alias:
            obj["private_key"] = new_private_key
            save_private_key_manager_data(data)
            return True
    print("Alias not found.")
    return False

def delete_private_key_object(alias):
    data = load_private_key_manager_data()
    updated_data = [obj for obj in data if obj["alias"] != alias]
    if len(updated_data) != len(data):
        save_private_key_manager_data(updated_data)
        return True
    else:
        print("Alias not found.")
        return False

def get_private_key_from_alias(alias):
    data = load_private_key_manager_data()
    for obj in data:
        if obj["alias"] == alias:
            return obj["private_key"]
    return None


# ============= Test ===============

try:
    add_private_key_object("Binance Private Key", "/home/user/desktop/")
    add_private_key_object("Coinbase Private Key", "key2")

    print(load_private_key_manager_data())

    print(get_private_key_from_alias("Binance Private Key"))
    print(get_private_key_from_alias("Coinbase Private Key"))
except Exception as e:
    print("An error occurred:", e)