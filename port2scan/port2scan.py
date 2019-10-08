from scapy.all import *
import sys
import os

opened = []

def tcpScan(ports):
    print ("+======================" + "="*len(sys.argv[1]) + "+")
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
        main()
