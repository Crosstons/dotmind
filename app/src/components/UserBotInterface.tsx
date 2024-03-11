'use client'
import { useState, useEffect } from 'react';
import axios from 'axios';
import Image from "next/image";
import Ava from '../../public/Avatar.png';
import logo from '../../public/logo.png';
import Footer from "@/components/footer";

const dummyTexts = [
  "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Reprehenderit atque nihil labore porro expedita velit ad minus molestiae eaque, quia iste dolorem? Modi nobis laudantium corporis ducimus non enim rerum cumque cum repudiandae nulla? Iure, maxime fugiat ut eaque rem velit, aliquid eos, corrupti id commodi neque pariatur repudiandae! Illum error aperiam quaerat possimus eum officia dolore eveniet?",
  "Lorem, ipsum dolor sit amet consectetur adipisicing.",
  "Hello."
];

const UserBotinterface = () => {
  const [currentTextIndex, setCurrentTextIndex] = useState(0);
  const [messages, setMessages] = useState([
    {
    "prompt": "Loading...",
    "response": "Loading...",
    "timestamp": "2000-01-01 00:00:00.00000"
    }
  ]);
  const [newMessage, setNewMessage] = useState('');

  useEffect(() => {
    // Fetch initial messages from the server or load from the JSON file
    const fetchMessages = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/chat_history/'); // Adjust the API endpoint accordingly
        setMessages(response.data);
        setCurrentTextIndex(response.data.length - 1);
        console.log(response);
      } catch (error) {
        console.error('Error fetching messages:', error);
      }
    };

    fetchMessages();
  }, []);

  const handleNextText = () => {
    setCurrentTextIndex(prevIndex => (prevIndex + 1) % dummyTexts.length);
  };

  const handlePreviousText = () => {
    setCurrentTextIndex(prevIndex =>
      prevIndex === 0 ? dummyTexts.length - 1 : prevIndex - 1
    );
  };

  return (
    <div className="">
      <div className="flex flex-col items-center justify-start min-h-screen bg-gray-100">
        {/* First div element */}
  	{/** Run the for loop here */}
  	{messages.map((msg,index) => (
        <>
        <div className="flex flex-col items-start" key={msg['timestamp']}>
          <div className="flex flex-col items-start justify-center rounded-lg p-6 min-w-[550px] max-w-[600px]">
            {/* Circle avatars */}
            <div className="flex items-center mb-4">
              <div className="bg-gray-300 w-12 h-12  flex items-center justify-center mr-4 mb-2 rounded-full">
                <Image
                  src={Ava}
                  alt="Avatar"
                  className="w-10 h-10 rounded-full"
                />
              </div>
            </div>
            {/* Name and dummy text */}
            <div>
              <p className="font-semibold text-lg mb-1">User</p>
              <div className="max-w-lg overflow-hidden bg-gray-200 rounded-lg w-full">
                <p className="p-4 text-gray-600">{msg['prompt']}</p>
              </div>
            </div>
          </div>

          {/* Second div element */}
          <div className="flex flex-col items-start justify-center rounded-lg p-6 min-w-[550px] max-w-[600px]">
            {/* Circle avatars */}
            <div className="flex items-center mb-4">
              <div className="bg-gray-300 w-12 h-12 rounded-full flex items-center justify-right mr-4">
                <Image
                  src={logo}
                  alt="Logo"
                  className="w-12 h-12"
                />
              </div>
            </div>
            {/* Name and dummy text */}
            <div>
              <p className="font-semibold text-lg mb-1">DotMind</p>
              <div className="max-w-lg overflow-hidden bg-white rounded-lg w-full">
                <p className="p-4 text-gray-600">{msg['response']}</p>
              </div>
            </div>
          </div>
        </div>
        </>
        ))}
      </div>
    </div>
  );
};

export default UserBotinterface;
