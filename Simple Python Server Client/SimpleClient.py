#!c:\Python27\python.exe

'''
Author: Glyph
Description: This is a simple TCP client which can be used to connect to a specified IP and PORT as provided by the user

NOTES: This Simple Client was built using a windows platform. Be sure to update the SHE BANG line to include a Linux
path where necessary.
'''

import sys
import socket

def Main():
	host = str(sys.argv[1])
	port = int(sys.argv[2])
	s=socket.socket()
	s.connect((host, port))

	message = raw_input("glyph_client@> ")
	while message != 'q':
		s.send(message)
		data = s.recv(1024)
		message = raw_input("glyph_client@> ")

	s.close()

if __name__ == '__main__':
	if len(sys.argv) == 3:
		Main()
	else:
		print ("Usage: %s <host> <port>" %sys.argv[0])
