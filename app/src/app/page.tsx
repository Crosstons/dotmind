'use client'
import React, { useState } from 'react';

const ChatInterface = () => {
  const [showChat, setShowChat] = useState(false);
  const [chatMessages, setChatMessages] = useState([]);
  const [selectedOption, setSelectedOption] = useState('');

  const handlePromptClick = (option) => {
    setSelectedOption(option);
    setShowChat(true);
    // You can add logic to handle the specific prompt clicked and initiate the chat.
    // For now, let's simulate a chat response.
    setChatMessages([{ sender: 'ChatBot', message: `You selected option ${option}` }]);
  };

  const handleSendMessage = (message) => {
    // Here you can send the user's message to the ChatBot and receive a response.
    // For now, let's simulate a chat response.
    setChatMessages([...chatMessages, { sender: 'User', message }]);
    // Simulated ChatBot response
    setChatMessages([...chatMessages, { sender: 'ChatBot', message: `You said: "${message}"` }]);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-200">
      <div className="max-w-md p-6 bg-white rounded-md shadow-md">
        <img
          src="/your-logo.png" // replace with your logo path
          alt="Logo"
          className="mx-auto mb-4"
        />
        <p className="text-center text-lg font-semibold mb-4">
          How can I help you today?
        </p>
        <div className="grid grid-cols-2 gap-4">
          <button
            className="bg-blue-500 text-white py-2 px-4 rounded-md"
            onClick={() => handlePromptClick('1')}
          >
            Option 1
          </button>
          <button
            className="bg-green-500 text-white py-2 px-4 rounded-md"
            onClick={() => handlePromptClick('2')}
          >
            Option 2
          </button>
          <button
            className="bg-yellow-500 text-white py-2 px-4 rounded-md"
            onClick={() => handlePromptClick('3')}
          >
            Option 3
          </button>
          <button
            className="bg-red-500 text-white py-2 px-4 rounded-md"
            onClick={() => handlePromptClick('4')}
          >
            Option 4
          </button>
        </div>
      </div>

      {showChat && (
        <div className="mt-4 max-w-md p-6 bg-white rounded-md shadow-md">
          <div className="space-y-4">
            {chatMessages.map((msg, index) => (
              <div key={index} className={msg.sender === 'User' ? 'text-right' : 'text-left'}>
                <span className="font-semibold">{msg.sender}: </span>
                <span>{msg.message}</span>
              </div>
            ))}
          </div>
          <div className="flex mt-4">
            <input
              type="text"
              placeholder="Type your message..."
              className="flex-1 p-2 border border-gray-300 rounded-l-md focus:outline-none"
              onKeyDown={(e) => {
                if (e.key === 'Enter') {
                  handleSendMessage(e.target.value);
                  e.target.value = '';
                }
              }}
            />
            <button
              className="bg-blue-500 text-white px-4 py-2 rounded-r-md"
              onClick={() => {
                const messageInput = document.getElementById('messageInput');
                if (messageInput) {
                  handleSendMessage(messageInput.value);
                  messageInput.value = '';
                }
              }}
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatInterface;
