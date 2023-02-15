import socket

my_address = '10.33.16.111'
port = 13000

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((my_address, port))
    print(f"Server is ready on {my_address}:{port}")
    try:
        while True:
            message, client_address = server_socket.recvfrom(1024)
            message = message.decode()
            response = ''.join(list(map(lambda ch: '' if ch in 'aeiou' else ch, message)))
            server_socket.sendto(response.encode(), client_address)
    except KeyboardInterrupt as ki:
        print("Shutting down...")
    finally:
        server_socket.close()
