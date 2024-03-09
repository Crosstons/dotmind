import json
import os

FILENAME = './db_json/json_files/address_book.json'

def load_address_book_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return []

def save_address_book_data(data):
    try:
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print("Error saving data:", e)

def add_json_object(alias, address):
    data = load_address_book_data()
    if not any(obj["alias"] == alias for obj in data):
        new_object = {"alias": alias, "address": address}
        data.append(new_object)
        save_address_book_data(data)
        return True
    else:
        print("Alias already exists.")
        return False

def update_json_object(alias, new_address):
    data = load_address_book_data()
    for obj in data:
        if obj["alias"] == alias:
            obj["location"] = new_address
            save_address_book_data(data)
            return True
    print("Alias not found.")
    return False

def delete_json_object(alias):
    data = load_address_book_data()
    updated_data = [obj for obj in data if obj["alias"] != alias]
    if len(updated_data) != len(data):
        save_address_book_data(updated_data)
        return True
    else:
        print("Alias not found.")
        return False

def get_value_from_key(key):
    data = load_address_book_data()
    for obj in data:
        if obj["alias"] == key:
            return obj["address"]
    return None


# ============= Test ===============

# try:
#     add_json_object("Binance Address", "home/desktop/binance")
#     add_json_object("Coinbase Address", "home/desktop/coinbase")

#     print(load_address_book_data())

#     print(get_value_from_key("Binance Address"))
#     print(get_value_from_key("Coinbase Address"))
# except Exception as e:
#     print("An error occurred:", e)