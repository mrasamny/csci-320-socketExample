import socket

my_address = '127.0.0.1'
port = 13000

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((my_address, port))
    print(f"Server is ready on {my_address}:{port}")
    try:
        while True:
            message, client_address = server_socket.recvfrom(1024)
            size = message[:4]
            message = message[4:]
            size = int.from_bytes(size, byteorder='big')
            print(f'size = {size} and message = {message}')
            # message, client_address = server_socket.recvfrom(size)
            message = message.decode()
            response = ''.join(list(map(lambda ch: '' if ch in 'aeiou' else ch, message)))
            print(message+":"+response)
            server_socket.sendto(response.encode(), client_address)
    except KeyboardInterrupt as ki:
        print("Shutting down...")
    finally:
        server_socket.close()
