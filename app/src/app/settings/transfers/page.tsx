import React from 'react';
import transferData from '../../../../../backend/db_json/json_files/transfer_manager.json'
const TransferPage = () => {
  return (
    <>
      <span className="font-bold text-4xl">Scheduled Transfers</span>

      <div className="bg-white shadow-md rounded my-6">
      <table className="min-w-max w-full table-auto">
        <thead>
          <tr className="bg-gray-100 text-gray-800 uppercase text-sm leading-normal">
            <th className="py-3 px-6 text-left">Time</th>
            <th className="py-3 px-6 text-left">To</th>
            <th className="py-3 px-6 text-left">Amount</th>
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm font-light">
          {transferData.map(transfer => (
            <tr key={transfer.time} className="border-b border-gray-200 hover:bg-gray-100">
              <td className="py-3 px-6 text-left whitespace-nowrap">{transfer.time}</td>
              <td className="py-3 px-6 text-left whitespace-nowrap">{transfer.to}</td>
              <td className="py-3 px-6 text-left whitespace-nowrap">{transfer.amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </>
  );
};

export default TransferPage;
