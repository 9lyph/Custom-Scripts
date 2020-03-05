#!/usr/bin/env python3
import requests
import socket
import os
import nmap
import getopt
import sys
import re

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

s = socket.socket()
nm = nmap.PortScanner()
global ports
ports = []
global input_file
input_file = ""
global output_file
output_file = ""
global terminal
terminal = False
global sorted_hrefs


def banner():
    os.system('clear')
    print("+---------------+")
    print("| URL 2 SCRAPER |")
    print("+---------------+\n")
    print ("----------------------------------------------------------------------|")
    print ("| Author: glyph                                                       |")
    print ("| Title: url2scraper.py                                               |")
    print ("| Creation Date: 11/06/2019                                           |")
    print ("| Version Control: 1.0 - Draft Concept                                |")
    print ("| Description: Takes a host file and scrapes the website using GET    |")
    print ("----------------------------------------------------------------------|")

def usage():
    print ("Usage: " + sys.argv[0] + " -i <host file> -o <output file> -t")
    print (f"Example: {sys.argv[0]} -i host.txt -o output.txt -t")

def main(input_file, output_file, terminal):
    with open (input_file, 'r') as f:
        print ("[+] Scraping Websites for embedded HTTP References")
        for line in f.readlines():
            url = line.strip()
            try:
                r = requests.head("http://"+url, timeout=1)
                if r.status_code == 301 or r.status_code == 302:
                    r = requests.get("https://"+url, timeout=1)
                    if r.status_code == 200:
                        print (f"[+] Host: {url}")
                        print (f"[+] Looking for embedded URL references on {url}")
                        hrefs = re.findall ('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
                        sorted_hrefs = set(hrefs)
                        if terminal == True:
                            print ("[+] Writing to terminal")
                            terminal = False
                            for href in sorted_hrefs:
                                print (href)
                        else:
                            with open (output_file, 'a') as output:
                                print ("[+] Writing results to file %s") %(sys.argv[4])
                                for href in set(sorted_hrefs):
                                    output.write(href+'\n')
                elif r.status_code == 200:
                    r = requests.get("http://"+url, timeout=1)
                    print ("[+] Looking for embedded URL references on %s") %(url)
                    hrefs = re.findall ('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
                    sorted_hrefs = set(hrefs)
                    if terminal == True:
                        print ("[+] Writing to terminal")
                        terminal = False
                        for href in sorted_hrefs:
                            print (href)
                    else:
                        with open (output_file, 'a') as output:
                            print ("[+] Writing results to file %s") %(sys.argv[4])
                            for href in set(sorted_hrefs):
                                output.write(href+'\n')
                else:
                    print ("[-] Host %s returned status %s") %(url,r.status_code)
            except:
                pass

if __name__=='__main__':
    banner()
    if len(sys.argv) <  3:
        usage()
    else:
        try:
            opts, args = getopt.gnu_getopt(sys.argv,"hio:t",["ifile=","ofile=","terminal="])
            for opt, arg in opts:
                if opt == "-h":
                    usage()
                    sys.exit()
                elif opt in ("-i", "--ifile"):
                    input_file = sys.argv[2]
                elif opt in ("-o", "--ofile"):
                    output_file = sys.argv[4]
                elif opt in ("-t", "--terminal"):
                    terminal = True
                else:
                    usage()
                    sys.exit()

            main(input_file, output_file, terminal)

        except getopt.GetoptError as err:
            print (err)
            usage()
            sys.exit(2)

