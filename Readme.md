# 🖥️ Chat Server and Client 🚀

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

A simple multi-client chat server built using **Python's socket and threading modules**. This project demonstrates how a server can handle multiple clients, broadcast messages, and enable real-time communication.  
[Project Link](https://roadmap.sh/projects/broadcast-server)

---

## 🌟 Features

- 🛠️ **Multi-client Support**: Handles multiple clients simultaneously.
- 📡 **Broadcast Messaging**: Messages sent by a client are broadcast to all other connected clients.
- 🔒 **Graceful Disconnection**: Clients can disconnect without crashing the server.
- 🎨 **Simple Design**: Easy-to-understand Python code for beginners.

---

## 🚀 How to Run

### 🧑‍💻 Server Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/chat-server.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chat-server
   ```

3. Start the server:
   ```bash
   python server.py
   ```
   The server will start listening for client connections on **localhost:4444**.

---

### 👥 Client Setup

1. Start a client:

   ```bash
   python client.py
   ```

2. Type your messages and hit **Enter** to send them.

3. To exit the chat, type:
   ```
   exit
   ```

---

## 📂 Project Structure

```
chat-server/
│
├── server.py   # Server script
├── client.py   # Client script
└── README.md   # Project documentation
```

---

## ✨ Example Usage

### Server Console:

```plaintext
Server Started !!
New connection: ('127.0.0.1', 56789)
Message from ('127.0.0.1', 56789): Hello
```

### Client Console:

```plaintext
Connected to the server!
Server: Welcome to the Server!
Type a message (or 'exit' to disconnect): Hi everyone!
Server: Hi everyone!
```

---

## 🛠️ Tech Stack

- **Python** 🐍
- **Socket Programming** 📡
- **Threading** 🧵

---

## 🎯 Future Improvements

- 🔒 Add user authentication.
- 🌍 Support for remote servers.
- 💬 Add chat room functionality.
- 📊 Integrate a simple GUI.

---
