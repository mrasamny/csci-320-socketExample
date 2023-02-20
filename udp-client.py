import socket

server_address = '127.0.0.1'
port = 13000

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input("What's your message: ")
    size = len(message).to_bytes(4, byteorder='big')
    client_socket.sendto(size + message.encode(), (server_address, port))
    response, address = client_socket.recvfrom(1024)
    print(f'Response from {address[0]} is "{response.decode()}"')
    client_socket.close()
