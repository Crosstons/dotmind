import React from 'react';
import addressBook from '../../../../../backend/db_json/json_files/address_book.json'

const AddressBookPage = () => {
  return (
    <>
      <span className="font-bold text-4xl">Account</span>

      <div className="bg-white shadow-md rounded my-6">
      <table className="min-w-max w-full table-auto">
        <thead>
          <tr className="bg-gray-100 text-gray-800 uppercase text-sm leading-normal">
            <th className="py-3 px-6 text-left">Name</th>
            <th className="py-3 px-6 text-left">Wallet Address</th>
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm font-light">
          {addressBook.map(user => (
            <tr key={user.alias} className="border-b border-gray-200 hover:bg-gray-100">
              <td className="py-3 px-6 text-left whitespace-nowrap">{user.alias}</td>
              <td className="py-3 px-6 text-left whitespace-nowrap">{user.address}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </>
  );
};

export default AddressBookPage;
