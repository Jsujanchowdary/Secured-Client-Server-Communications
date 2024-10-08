# Encrypted TCP and UDP Server-Client Communication

This repository contains a Python implementation of encrypted communication between TCP and UDP servers and clients using Caesar Cipher for encryption.

## Features

- **TCP Server-Client Communication:**
  - The server and client communicate using TCP sockets.
  - Messages are encrypted using a Caesar Cipher with a configurable shift value.
  - The client sends an encrypted message to the server, which decrypts it, processes it, and sends an encrypted response back.

- **UDP Server-Client Communication:**
  - The server and client communicate using UDP sockets.
  - Similar to TCP, the messages are encrypted using the Caesar Cipher.
  - The server decrypts incoming messages, processes them, and responds with an encrypted message.

## Prerequisites

You need to have Python 3.x installed on your machine.

## Running the Scripts

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jsujanchowdary/Secured-Client-Server-Communications.git
   cd Secured-Client-Server-Communications
   ```

2. **Run the script:**
   ```bash
   python3 main.py
   ```

3. **Select the desired component:**
   - `1` for TCP Server
   - `2` for TCP Client
   - `3` for UDP Server
   - `4` for UDP Client

### Example Usage

#### TCP Communication

1. Run the TCP server:
   ```bash
   python3 main.py
   # Choose option 1 (TCP Server)
   ```

2. In another terminal, run the TCP client:
   ```bash
   python3 main.py
   # Choose option 2 (TCP Client)
   ```

You should see encrypted and decrypted messages exchanged between the server and client.

#### UDP Communication

1. Run the UDP server:
   ```bash
   python3 main.py
   # Choose option 3 (UDP Server)
   ```

2. In another terminal, run the UDP client:
   ```bash
   python3 main.py
   # Choose option 4 (UDP Client)
   ```

You will see a similar exchange of encrypted and decrypted messages.

## Code Overview

### Caesar Cipher

A basic Caesar Cipher is implemented in the `encrypt()` and `decrypt()` functions. These functions are used to encrypt outgoing messages and decrypt incoming ones in both TCP and UDP communications.

### TCP Communication

- **TCP Server:**
  - Binds to a local address and port, listens for incoming connections.
  - Receives encrypted messages, decrypts them, processes them, and sends an encrypted response.

- **TCP Client:**
  - Connects to the server, sends an encrypted message, and receives an encrypted response.

### UDP Communication

- **UDP Server:**
  - Listens for incoming messages on a specific port.
  - Receives encrypted messages, decrypts them, and sends an encrypted response.

- **UDP Client:**
  - Sends an encrypted message to the server and waits for an encrypted response.
