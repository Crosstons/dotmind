import json
import os

def create_transfer_manager_file(filename):
    try:
        with open(filename, "w") as f:
            json.dump([], f)
    except IOError as e:
        print("Error creating file:", e)

def load_transfer_manager_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return []

def save_transfer_manager_data(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print("Error saving data:", e)

def schedule_transfer(filename, from_account, to_account, amount, time):
    data = load_transfer_manager_data(filename)
    new_transfer = {"from": from_account, "to": to_account, "amount": amount, "time": time}
    data.append(new_transfer)
    save_transfer_manager_data(filename, data)

def cancel_transfer(filename, from_account, to_account, time):
    data = load_transfer_manager_data(filename)
    data = [transfer for transfer in data if transfer["from"] != from_account or
            transfer["to"] != to_account or transfer["time"] != time]
    save_transfer_manager_data(filename, data)

def get_transfers_by_account(filename, account):
    data = load_transfer_manager_data(filename)
    transfers = [transfer for transfer in data if transfer["from"] == account or transfer["to"] == account]
    return transfers


# ============= Test ===============

filename = 'transfer_manager.json'

try:
    create_transfer_manager_file(filename)

    schedule_transfer(filename, "Account1", "Account2", 100, "2024-03-10 08:00:00")
    schedule_transfer(filename, "Account2", "Account3", 50, "2024-03-12 12:00:00")

    print(load_transfer_manager_data(filename))

    print(get_transfers_by_account(filename, "Account2"))

    cancel_transfer(filename, "Account2", "Account3", "2024-03-12 12:00:00")

    print(load_transfer_manager_data(filename))
except Exception as e:
    print("An error occurred:", e)