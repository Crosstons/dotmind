'use client'
import { useState } from 'react';
import Image from "next/image";
import Ava from '../../public/Avatar.png';
import logo from '../../public/logo.png';
import Footer from "@/components/footer";

const dummyTexts = [
  "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Reprehenderit atque nihil labore porro expedita velit ad minus molestiae eaque, quia iste dolorem? Modi nobis laudantium corporis ducimus non enim rerum cumque cum repudiandae nulla? Iure, maxime fugiat ut eaque rem velit, aliquid eos, corrupti id commodi neque pariatur repudiandae! Illum error aperiam quaerat possimus eum officia dolore eveniet?",
  "Lorem, ipsum dolor sit amet consectetur adipisicing."
];

const UserBotinterface = () => {
  const [currentTextIndex, setCurrentTextIndex] = useState(0);

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
        <div className="flex flex-col items-start">
          <div className="flex flex-col items-start justify-center bg-white rounded-lg shadow-md p-6 mb-6 min-w-[550px] max-w-[600px]">
            {/* Circle avatars */}
            <div className="flex items-center mb-4">
              <div className="bg-gray-300 w-12 h-12 rounded-full flex items-center justify-center mr-4">
                <Image
                  src={Ava}
                  alt="Avatar"
                  className="w-8 h-8 rounded-full"
                />
              </div>
            </div>
            {/* Name and dummy text */}
            <div>
              <p className="font-semibold text-lg mb-1">Name</p>
              <div className="max-w-lg overflow-hidden bg-gray-200 rounded-lg w-full">
                <p className="p-4 text-gray-600">{dummyTexts[currentTextIndex]}</p>
              </div>
            </div>
          </div>

          {/* Second div element */}
          <div className="flex flex-col items-start justify-center bg-gray-200 rounded-lg shadow-md p-6 min-w-[550px] max-w-[600px]">
            {/* Circle avatars */}
            <div className="flex items-center mb-4">
              <div className="bg-gray-300 w-12 h-12 rounded-full flex items-center justify-center mr-4">
                <Image
                  src={logo}
                  alt="Logo"
                  className="w-8 h-8"
                />
              </div>
            </div>
            {/* Name and dummy text */}
            <div>
              <p className="font-semibold text-lg mb-1">DotMind</p>
              <div className="max-w-lg overflow-hidden bg-gray-100 rounded-lg w-full">
                <p className="p-4 text-gray-600">{dummyTexts[currentTextIndex]}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserBotinterface;
