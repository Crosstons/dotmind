from datetime import datetime
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from db_json import address_book, private_key_manager, transfer_manager
from ai_llm.modules import read_pk
import schedule
import time
import json

def execute_transactions(transactions):
  current_time = datetime.now()
  for transaction in transactions:
    timestamp_str = transaction['time']
    timestamp_datetime = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')  # Match your time format
    timestamp_seconds = timestamp_datetime.timestamp()
    if timestamp_seconds <= current_time:
        print(f"Executing transaction: {transaction}")

        substrate = SubstrateInterface(transaction['rpc'])

        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer_allow_death',
            call_params={
                'dest': address_book.get_value_from_key(transaction['to']),
                'value': int(transaction['amount'])
            }
        )
        
        seed = read_pk(private_key_manager.get_private_key_from_alias("default"))

        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=Keypair.create_from_mnemonic(seed))

        try:
            receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)

            print('Extrinsic "{}" included in block "{}"'.format(
                receipt.extrinsic_hash, receipt.block_hash
            ))

            if receipt.is_success:

                print('✅ Success, triggered events:')
                for event in receipt.triggered_events:
                    print(f'* {event.value}')

            else:
                print('⚠️ Extrinsic Failed: ', receipt.error_message)

            # equivalent to removing the scheduled transfer from the storage after execution 
            transfer_manager.cancel_transfer("default", transaction['to'], transaction['time'])

        except SubstrateRequestException as e:
            print("Failed to send: {}".format(e))

def main():
  with open("./db_json/json_files/transfer_manager.json") as f:
    transactions = json.load(f)

  for transaction in transactions:
    _timestamp = transaction['time']
    schedule.every().hour.at(":00").do(execute_transactions, transactions)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()
