'use client'
import React, { useState } from 'react';
import { cn } from '@/lib/utils';
import { Button, buttonVariants } from './ui/button';


// Define your Footer component
const Footer = () => {
  // State to store the value of the input field
  const [inputValue, setInputValue] = useState('');

  // Function to handle changes in the input field
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };
  const handleSend = () => {
    console.log('Sending input value:', inputValue);

    setInputValue('');
  };

  return (
    <div className={cn('sticky bottom-0 z-30 w-full border-t bg-gray-100')}>
      <div className="flex items-center justify-between px-4 py-4">
        {/* Input field */}
        <input
          type="text"
          value={inputValue}
          onChange={handleChange}
          placeholder="Enter your message..."
          className="flex-grow p-2 border border-gray-300 rounded-l-md focus:outline-none"
        />

        {/* Send button */}
        <Button>
            Submit
        </Button>
      </div>
    </div>
  );
};

export default Footer;
