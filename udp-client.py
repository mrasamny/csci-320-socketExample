import socket

server_address = '10.33.16.111'
port = 13000

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input("What's your message: ")
    client_socket.sendto(message.encode(), (server_address, port))
    response, address = client_socket.recvfrom(1024)
    print(f'Response from {address[0]} is "{response.decode()}"')
    client_socket.close()
