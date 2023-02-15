# Exercise: Simple UDP Vowel Monster Server

The goal of this exercise is to create a simple UDP echo server. The server will receive a message from a client and send the same message back to the client.

### Step 1: Understanding the UDP Communication Model

UDP is a simple, connectionless, and unreliable protocol that allows applications to send and receive messages without establishing a connection. Unlike TCP, UDP does not guarantee that the messages will be delivered in order, or that they will be delivered at all.

### Step 2: Implementing the Server

The server should:

- Create a socket using the socket function.
- Bind the socket to a specific address and port using the `bind` function. 
- Receive messages from clients using the `recvfrom` function. 
- Send the message with all vowels removed back to the client using the sendto function. 

### Step 3: Implementing the Client

The client should:

- Create a socket using the socket function. 
- Send a message to the server using the `sendto` function. 
- Receive the response with missing vowels from the server using the `recvfrom` function. 
- Compare the received message with the original message to check for errors.

### Step 4: Testing Your Implementation

You can test your implementation by running the server and client on the same machine or on separate machines. Make sure to run the server first and then the client. You can use `nc` or `telnet` to act as a client and send messages to the server.

### Tips

- Make sure to handle errors in your code.
- Use `to_bytes` and `from_bytes` to convert to/from bytes form/to integer, if necessary.
- Make sure to select endianess when converting integer to byte.
