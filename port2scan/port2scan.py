from scapy.all import *
import sys
import os

def tcpScan(ports):
    print ("+======================" + "="*len(sys.argv[1]) + "+")
    print ("| TCP Scanning %s ") % sys.argv[1]
    print ("+======================" + "="*len(sys.argv[1]) + "+")
    for port in ports:
        p = IP(dst=sys.argv[1])/TCP(dport=int(port))
        ans,unans = sr(p, verbose=False, timeout=3)
        if ans:
            print ("[+] Port: %s reachable") % port
        else:
            print ("[-] Port: %s unreachable") % port


def main():
    ports = []
    for args in xrange(len(sys.argv)):
        ports.append(sys.argv[args])
    tcpScan(ports[2:])

if __name__=='__main__':
    main()
