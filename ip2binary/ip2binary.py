import os
import sys

''' ip2bin.py takes a IPv4 Address and converts the value to its binary equivalent '''
def banner():
	os.system('cls')
	print(" _        _____  _     _                        ")
	print("(_)      / __  \| |   (_)                       ")
	print(" _ _ __  `' / /'| |__  _ _ __   __ _ _ __ _   _ ")
	print("| | '_ \   / /  | '_ \| | '_ \ / _` | '__| | | |")
	print("| | |_) |./ /___| |_) | | | | | (_| | |  | |_| |")
	print("|_| .__/ \_____/|_.__/|_|_| |_|\__,_|_|   \__, |")
	print("  | |                                      __/ |")
	print("  |_|                                     |___/\n")
	print ("+------------------------------------------------------------------------------------------------------------------+")
	print ("| Author: glyph                                                                                                    |")
	print ("| Title: ip2binary.py                                                                                              |") 
	print ("| Creation Date: 20/02/2018                                                                                        |")
	print ("| Version Control: 1.0                                                                                             |") 
	print ("| Description: Takes an IP Address in dotted decimal notated form and converts it to its binary equivalent.        |")
	print ("| Usage: " + sys.argv[0][-12:] + " <ip_address to be converted>\t\t                                                   |")
	print ("+------------------------------------------------------------------------------------------------------------------+")

class format_not_acceptable(object):
	def __init__(self, octet, position):
		self.octet = octet
		self.position = position
	def format_output(self):
		print ("The " + self.position + " value " + "\'" + self.octet + "\'" + " is not within an acceptable 32bit IP Address Range.")

def usage():
	print ("Usage: " + sys.argv[0][-12:] + " <ip_address to be converted>")

def main(argv):
	banner()
	well_formed = True
	try:
		ip_address = str(argv[0])
		octet1, octet2, octet3, octet4 = ip_address.split('.')		
		if int(octet1) < 256:
			octet1_binary = bin(int(octet1))
		else:
			well_formed = False
			num1 = format_not_acceptable(octet1, '1st')
			num1.format_output()
		if int(octet2) < 256:
			octet2_binary = bin(int(octet2))
		else:
			well_formed = False
			num2 = format_not_acceptable(octet2, '2nd')
			num2.format_output()
		if int(octet3) < 256:
			octet3_binary = bin(int(octet3))
		else:
			well_formed = False
			num3 = format_not_acceptable(octet3, '3rd')
			num3.format_output()
		if int(octet4) < 256:
			octet4_binary = bin(int(octet4))
		else:
			well_formed = False
			num4 = format_not_acceptable(octet4, '4th')
			num4.format_output()
	
		if well_formed == True:
			line = "+==================================================================================================================+"
			print (line)
			print ("|" + "\n" + "|" + " " + "Original IP Address\n| " + ip_address + "\n" + "|")
			print ("|" + " " + "Binary (dotted notation)\n| %s.%s.%s.%s" % (octet1_binary[2:].zfill(8), octet2_binary[2:].zfill(8), octet3_binary[2:].zfill(8), octet4_binary[2:].zfill(8)) + "\n" + "|")
			print (line)
	except IndexError:
		usage()
	except ValueError:
		print ("\nIP Address " + "\'" + ip_address +"\'" + " does not look very well formed !")

if __name__ == '__main__':
	main(sys.argv[1:])