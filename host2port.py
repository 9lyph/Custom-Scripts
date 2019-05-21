import requests
import socket
import os
import nmap
import getopt
import sys

s = socket.socket()
nm = nmap.PortScanner()
global ports
ports = []
global input_file
input_file = ""

def banner():
    os.system('cls')
    print(" _    _   ____    _____  _______  ___   _____    ____   _____  _______ ")
    print("| |  | | / __ \  / ____||__   __||__ \ |  __ \  / __ \ |  __ \|__   __|")
    print("| |__| || |  | || (___     | |      ) || |__) || |  | || |__) |  | |   ")
    print("|  __  || |  | | \___ \    | |     / / |  ___/ | |  | ||  _  /   | |   ")
    print("| |  | || |__| | ____) |   | |    / /_ | |     | |__| || | \ \   | |   ")
    print("|_|  |_| \____/ |_____/    |_|   |____||_|      \____/ |_|  \_\  |_|   \n")
    print ("-------------------------------------------------------------------------------------------------------------------|")
    print ("| Author: glyph                                                                                                    |")
    print ("| Title: host2port.py                                                                                              |")
    print ("| Creation Date: 20/05/2019                                                                                        |")
    print ("| Version Control: 1.0 - Draft Concept                                                                             |")
    print ("| Description: Takes a host file, coupled with ports to scan and returns port status.                              |")
    print ("-------------------------------------------------------------------------------------------------------------------|")

def usage():
    print ("Usage: " + sys.argv[0] + " -i <host file> -p <ports>")
    print ("Example: %s -i host.txt -p 22,23,21") %sys.argv[0]

def main(file, ports):
    with open (file, 'r') as f:
        print "[+] Examining Port States"
        for line in f.readlines():
            url = line.strip()
        try:
            ip = socket.gethostbyname(url)
            print ("\nHost: %s\nIP: %s") %(url,ip)
            for port in ports:
                nm.scan(ip, port, arguments="-sS")
                state = nm[ip]['tcp'][int(port)]['state']
                if state == 'open':
                    print ("%s/tcp - open") %port
                elif state == 'filtered':
                    print ("%s/tcp - filtered") %port
                elif state == 'closed':
                    print ("%s/tcp - closed") %port
        except socket.gaierror:
            pass
        except:
            pass

if __name__=='__main__':
    banner()
    if len(sys.argv) == 5:
        try:
            opts, args = getopt.gnu_getopt(sys.argv,"hi:p",["ifile=","ports="])
            for opt, arg in opts:
                if opt == "-h":
                    usage()
                    sys.exit()
                elif opt in ("-i", "--ifile"):
                    input_file = arg
                elif opt in ("-p", "--ports"):
                    ports = sys.argv[4].split(',')
                else:
                    usage()
                    sys.exit()

            main(input_file, ports)

        except getopt.GetoptError as err:
            print (err)
            usage()
            sys.exit(2)
    else:
        usage()
        sys.exit()