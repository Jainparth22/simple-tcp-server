import socket

def start_server(host='0.0.0.0', port=8080):
    # Step 1: Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Step 2: Bind the socket to an address and port
    server_socket.bind((host, port))
    
    # Step 3: Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}")

    while True:
        try:
            # Step 4: Accept a connection
            client_socket, client_address = server_socket.accept()
            
            # Step 5: Log the client's IP address
            print(f"Client connected from {client_address[0]}:{client_address[1]}")
            
            # Step 6: Close the connection
            client_socket.close()
        except KeyboardInterrupt:
            print("\nShutting down the server...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    # Step 7: Close the server socket
    server_socket.close()

if __name__ == "__main__":
    start_server()