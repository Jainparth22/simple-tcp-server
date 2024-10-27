# Simple TCP Server

This project implements a simple TCP server in Python that listens for incoming connections, logs a message upon connection, and then closes the connection.

## Features

- Listens on a specified port (default: 8080)
- Logs a message to the console when a client connects, showing the client's IP address and port
- Closes the connection after logging the message
- Graceful shutdown with Ctrl+C

## Requirements

- Python 3.x

## Installation

No additional installation is required beyond having Python installed on your system.

## Usage

1. Clone this repository or download the `tcp_server.py` file.

2. Open a terminal or command prompt.

3. Navigate to the directory containing `tcp_server.py`.

4. Run the server with the following command:

   ```
   python tcp_server.py
   ```

5. The server will start and display a message indicating it's listening:

   ```
   Server is listening on 0.0.0.0:8080
   ```

6. To test the server, you can use a tool like `telnet` or `nc` (netcat) from another terminal:

   ```
   nc localhost 8080
   ```

   or

   ```
   telnet localhost 8080
   ```

7. You should see a message in the server's console indicating a client has connected, showing their IP address and port.

8. To stop the server, press Ctrl+C in the terminal where the server is running.

## Customization

You can modify the host and port in the `tcp_server.py` file by changing the default values in the `start_server` function:

```python
def start_server(host='0.0.0.0', port=8080):
```

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Author

[Your Name]

## Acknowledgments

- Python Socket Programming documentation
- [Any other resources or inspirations you used]