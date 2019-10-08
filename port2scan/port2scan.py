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
	print ("| Usage: " + sys.argv[0] + " <host> [<ports seperated by spaces>]\t\t                                                 |")
	print ("+------------------------------------------------------------------------------------------------------------------+")

def tcpScan(ports):
    print ("\n+======================" + "="*len(sys.argv[1]) + "+")
    print ("| TCP Scanning %s ") % sys.argv[1]
    print ("+======================" + "="*len(sys.argv[1]) + "+\n")
    print ("PORT(tcp)\tSTATE")
    print ("---------\t-----")
    for port in ports:
        p = IP(dst=sys.argv[1])/TCP(dport=int(port))
        ans,unans = sr(p, verbose=False, timeout=3)
        if ans:
            print ("%s\t\topen ") % port
#            print ("[+] Port: %s reachable") % port
        else:
            pass
#            print ("[-] Port: %s unreachable") % port

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
