from scapy.all import *
import sys
import os

def banner():
	os.system('clear')
        print("                  _   _____")
        print("                 | | / __  |")
        print(" _ __   ___  _ __| |_   / / ___  ___ __ _ _ __")
        print("|  _ \ / _ \|  __| __| / / / __|/ __/ _  |  _ ")
        print("| |_) | (_) | |  | |_./ /__\__ \ (_| (_| | | | |")
        print("|  __/ \___/|_|   \__\_____/___/\___\__ _|_| |_|")
        print("| |                                             ")
        print("|_|\n")
	print ("+------------------------------------------------------------------------------------------------------------------+")
	print ("| Author: glyph                                                                                                    |")
	print ("| Title: port2scan.py                                                                                              |") 
	print ("| Creation Date: 08/10/2019                                                                                        |")
	print ("| Version Control: 1.0                                                                                             |") 
	print ("| Description: Quick and dirty Active TCP Scanner.                                                                 |")
	print ("| Usage: " + sys.argv[0] + " <host> [<ports seperated by spaces>]\t\t                                              |")
        print ("| Example: " + sys.argv[0] + " 192.168.1.1 80 443                                                               |")
	print ("+------------------------------------------------------------------------------------------------------------------+")

def tcpScan(ports):
    print ("Scanning: %s") % sys.argv[1]
    try:
        for port in ports:
            p = sr1(IP(dst=sys.argv[1])/TCP(sport=RandShort(),dport=int(port),flags="S"),verbose=False, timeout=3)
            try:
                if p.getlayer(TCP).flags == "SA":
                    print ("[+] %s Open") % port
                elif p.getlayer(TCP).flags == "R":
                    print ("[+] %s Filtered") % port
            except AttributeError:
                print ("[+] %s Closed") % port
    except socket.gaierror:
        pass

def main():
    ports = []
    for args in xrange(len(sys.argv)):
        ports.append(sys.argv[args])
    tcpScan(ports[2:])

if __name__=='__main__':
    if len(sys.argv) < 3:
        print ("\nUsage: %s <host> <[ports seperated by spaces]>") %(sys.argv[0])
        print ("Example: %s 192.168.1.1 80 443") %(sys.argv[0])
    else:
        banner()
        main()

