import socket
import threading

def receive_messages(client_socket):
    """
    Listen for messages from the server and display them.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"Server: {message}")
            else:
                print("Server closed the connection.")
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

host = "localhost"
port = 4444

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((host, port))
    print("Connected to the server!")
    
    # Start a thread to listen for messages from the server
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    # Main loop for sending messages to the server
    while True:
        user_input = input("Type a message (or 'exit' to disconnect): ")
        if user_input.lower() == "exit":
            client_socket.close()
            print("Disconnected from the server.")
            break
        else:
            try:
                client_socket.send(bytes(user_input, "utf-8"))
            except Exception as e:
                print(f"Error sending message: {e}")
                break

except ConnectionRefusedError:
    print("Could not connect to the server. Make sure the server is running.")
