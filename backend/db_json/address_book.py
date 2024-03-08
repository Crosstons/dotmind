import json
import os

def create_address_book_file(filename):
    try:
        with open(filename, "w") as f:
            json.dump([], f)
    except IOError as e:
        print("Error creating file:", e)

def load_address_book_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return []

def save_address_book_data(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print("Error saving data:", e)

def add_json_object(filename, alias, location):
    data = load_address_book_data(filename)
    new_object = {"alias": alias, "location": location}
    data.append(new_object)
    save_address_book_data(filename, data)

def update_json_object(filename, alias, new_location):
    data = load_address_book_data(filename)
    for obj in data:
        if obj["alias"] == alias:
            obj["location"] = new_location
            break
    save_address_book_data(filename, data)

def delete_json_object(filename, alias):
    data = load_address_book_data(filename)
    data = [obj for obj in data if obj["alias"] != alias]
    save_address_book_data(filename, data)

def get_value_from_key(filename, key):
    data = load_address_book_data(filename)
    for obj in data:
        if obj["alias"] == key:
            return obj["location"]
    return None


# ============= Test ===============

filename = 'address_book.json'

try:
    create_address_book_file(filename)

    add_json_object(filename, "Binance Address", "home/desktop/binance")
    add_json_object(filename, "Coinbase Address", "home/desktop/coinbase")

    print(load_address_book_data(filename))

    print(get_value_from_key(filename, "Binance Address"))
    print(get_value_from_key(filename, "Coinbase Address"))
except Exception as e:
    print("An error occurred:", e)