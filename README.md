<div align="center">
    <img src="./app/public/logo.svg" alt="DotMind" height="100" width="100" />
<h1 align="center">
    DotMind : An Agent Built For Substrates
</h1>

 Bringing The AI Revolution To The Polkadot Ecosystem - An Agent To Make Things Simpler

[Demo](https://youtu.be/d3X5tAOxRRk?feature=shared)&nbsp;&nbsp;•&nbsp;&nbsp;
[Figma](https://www.figma.com/file/Yf1ieeMtQUIQOpniDKJZOx/DotMind?type=design&mode=design)

</div>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Features](#features)
- [Current Capabilities](#current-capabilities)
- [Future Scope](#future-scope)
- [Tech Stack](#tech-stack)
- [Modularity](#modularity)
- [Installation Steps](#installation-steps)
- [Guidelines for prompts](#guidelines-for-prompts)
- [License](#license)
- [Contribution Guidelines](#contribution-guidelines)

## Problem Statement

The current interaction with the Polkadot ecosystem involves complexities that hinder user engagement. Our solution, DotMind, addresses these challenges by introducing AI agents capable of performing various tasks, streamlining the user experience while maintaining the security of keypairs and privacy of the users.

## Features

- **Onboarding New Users**: DotMind simplifies the interaction process, reducing the learning curve associated with blockchain technology, thus making it easier for new users to engage with the Polkadot ecosystem.
- **Simplified Interactions**: DotMind enables users to perform tasks such as keypair management, balance queries, transfers, and price checks through a user-friendly chatbot interface, enhancing accessibility and usability.

## Current Capabilities

- **Keypair Management**: Create, delete, and rename private keys and account addresses.
- **Query Balances On-Chain**: Fetch balances of accounts across different Polkadot Parachains.
- **Scheduled and Instant Transfers**: Facilitate both scheduled and instant transfers of assets or funds.
- **Price Check**: Fetch USD prices from Coinbase API for major cryptocurrencies.

## Future Scope

In the future, DotMind aims to expand its capabilities to include DEX trades, basic token interactions, flexible contract interactions, and more. Additionally, we plan to enhance security and privacy by implementing local and lightweight computation and fine tuning AI models.

## Tech Stack

- **Frontend**: Node.js, npm
- **Backend**: Flask, LLM
- **APIs**: Coinbase

## Modularity

DotMind is designed with modularity in mind, allowing developers to easily build upon and extend its functionality. By providing clear guidelines for prompts and interactions, developers can integrate additional features, customize user experiences, and contribute to the project's growth.

## Installation Steps

Before running the project locally, ensure you have the following prerequisites installed:

- `Node.js`
- `npm`
- `Rust`
- `Python`

1. Open two terminal windows.

2. In the first terminal, navigate to the backend directory:

   ```bash
   cd backend
   ```

3. Install backend dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the backend server:

   ```bash
   python main.py
   ```

5. In the second terminal, navigate to the app directory:

   ```bash
   cd app
   ```

6. Install frontend dependencies:

   ```bash
   npm install
   ```

7. Start the frontend:
   ```bash
   npm run dev
   ```

## Guidelines for prompts

- When adding a new address to the address book, ensure that the address is enclosed in single inverted commas.
- Avoid using direct addresses for transfers or scheduled transfers. Instead, use an Alias that has been registered in the address book.
- All transactions will be signed with an Alias named "default" in the private keys file for now.
- Please include decimal zeros when entering a transfer prompt for now.
- Start a scheduled transfer instruction with 'timed transfer - ....'

## License

This project is licensed under the MIT

## Contribution Guidelines

DotMind is open-source and welcomes contributions from the community. Developers can collaborate, submit bug fixes, suggest new features, and contribute to improving the overall reliability, security, and usability of the project.
