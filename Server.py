#!/usr/bin/python3

import socket

#made socket object
serversocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444 

#binding to socket
serversocket.bind((host, port))

#start TCP listener
serversocket.listen(3)

while True:
    #starting the connection
    clientsocket, address = serversocket.accept()
    print("received connection from" % str(address))

    message = 'Hello! Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close

