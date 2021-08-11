# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# import modules
import socket
import threading

""" A thread is a separate flow of execution """

# specify target ip and port
IP = '0.0.0.0'
PORT = 9999

def main():
    # create server object and listen on specified port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = ipv4, SOCK_STREAM = tcp
    server.bind((IP, PORT))
    server.listen(5)

    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # wait for an incomng connection
        client, address = server.accept() 
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main() 

# test with a 2nd shell, type 'telnet localhost 9999' and then on next line add text
# also you can get similar with results with netcat as a listener, but this may be removed on secure machines
