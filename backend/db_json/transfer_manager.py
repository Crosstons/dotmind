import json
import os

FILENAME = './db_json/json_files/transfer_manager.json'

def load_transfer_manager_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Error loading data:", e)
        return []

def save_transfer_manager_data(data):
    try:
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print("Error saving data:", e)

def schedule_transfer(from_account, to_account, amount, time):
    data = load_transfer_manager_data()
    new_transfer = {"from": from_account, "to": to_account, "amount": amount, "time": time}
    data.append(new_transfer)
    save_transfer_manager_data(data)

def cancel_transfer(from_account, to_account, time):
    data = load_transfer_manager_data()
    data = [transfer for transfer in data if transfer["from"] != from_account or
            transfer["to"] != to_account or transfer["time"] != time]
    save_transfer_manager_data(data)

def get_transfers_by_account(account):
    data = load_transfer_manager_data()
    transfers = [transfer for transfer in data if transfer["from"] == account or transfer["to"] == account]
    return transfers


# ============= Test ===============

# try:
#     schedule_transfer("Account1", "Account2", 100, "2024-03-10 08:00:00")
#     schedule_transfer("Account2", "Account3", 50, "2024-03-12 12:00:00")

#     print(load_transfer_manager_data())

#     print(get_transfers_by_account("Account2"))

#     cancel_transfer("Account2", "Account3", "2024-03-12 12:00:00")

#     print(load_transfer_manager_data())
# except Exception as e:
#     print("An error occurred:", e)