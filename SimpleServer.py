#!c:\Python27\python.exe

'''
Author: Glyph
Description: This is a simple TCP server which can be invoked on an IP and PORT provided by the user

NOTES: This Simple Server was built using a windows platform. Be sure to update the SHE BANG line to include a Linux
path where necessary.
'''

import socket
import sys

def Main():
	#Defining a socket to be used with the server
	#Invoking of the socket method takes 2 arguments, defaults to socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Server Started:\n")
	host = str(sys.argv[1])
	port = int(sys.argv[2])
	s = socket.socket()
	#Now we need to bind the socket to an IP address and port
	s.bind((host, port))
	#Now we need to listen for incoming connections, and we provide how many sockets to listen for
	s.listen(1)

	#We now need to set the server up to accept a socket from the client
	#The accept blocks and waits for an incoming connection. When the client connects it returns a new socket object which represents the client connection
	connection, address = s.accept()
	
	#In order to simulate a server experience, we can setup an While Loop that receives client data and sends this "feedback" back the client
	banner = ("~"*48 + "\n" + "Welcome to GLYPH - Stay awhile ! Stay Forever !\n" + "~"*48 + "\n")
	banner += ("Client %s connected." %str(address))
	print (banner)
	while True:
		data = connection.recv(1024)
		if not data:
			break
		print ("glyph_server@> " + str(data))
		connection.send(data)

	#In order to shutdown the client connection cleanly, we need to close the session ("TCP FIN")
	print ("Client %s closed connection." %str(address))
	connection.close()

if __name__ == '__main__':
	if len(sys.argv) == 3:
		Main()
	else:
		print ("Usage: %s <host> <port> " %sys.argv[0])
