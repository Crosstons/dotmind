import React from 'react';
import keyPairsData from '../../../../../backend/db_json/json_files/private_key_manager.json'

const KeypairPage = () => {
  return (
    <>
      <span className="font-bold text-4xl">Key Pair</span>
      <div className="bg-white shadow-md rounded my-6">
      <table className="min-w-max w-full table-auto">
        <thead>
          <tr className="bg-gray-100 text-gray-800 uppercase text-sm leading-normal">
            <th className="py-3 px-6 text-left">Alias</th>
            <th className="py-3 px-6 text-left">File Location</th>
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm font-light">
          {keyPairsData.map(pair => (
            <tr key={pair.alias} className="border-b border-gray-200 hover:bg-gray-100">
              <td className="py-3 px-6 text-left whitespace-nowrap">{pair.alias}</td>
              <td className="py-3 px-6 text-left whitespace-nowrap">{pair.private_key}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </>
  );
};

export default KeypairPage;
