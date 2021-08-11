# tcp client 
import socket

RHOST = 'books.toscrape.com'
RPORT = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to the socket
client.connect((RHOST,RPORT))

# send some data !
# see : https://stackoverflow.com/questions/34192093/python-socket-get

# format the request
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % RHOST

# encode the string to bytes and...SEND
client.send(request.encode()) 

# object to receive the response
response = client.recv(4096)

# decode and print the response
print(response.decode())

client.close(
