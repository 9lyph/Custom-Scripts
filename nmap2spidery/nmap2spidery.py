#!/usr/bin/env python3

import os
import nmap3
import getopt
import sys
import json
from collections import Counter

'''
Script Usage
============

Requirements: 
Creating Requirement File
1. Setup Python3 virtual environment
    - python3 -m venv nmap2spidery
2. Install required modules
    - python3 -m pip install python3-nmap
    - python3 -m pip install simplejson
3. Freeze virtual environment
    - python3 -m pip freeze > requirements.txt

Installation of app
    - python3 -m pip install -r requirements.txt
    cat requirements
        python3-nmap==1.4.1
        simplejson==3.17.0
'''

## Declaring Variables
global nm
nm = nmap3.NmapScanTechniques()
global nmap
nmap = nmap3.Nmap()
global ports
ports = []
global default_file
default_file = "spidery_goodness.txt"
global network
network = ""
global output_file
output_file = default_file
global input_file
input_file = ""
global top_ports
top_ports = []


def banner():
    os.system('clear')
    print("+---------------+")
    print("| NMAP2SPIDERY  |")
    print("+---------------+\n")
    print ("+--------------------------------------------------------------------------------------------+")
    print ("| Author: glyph                                                                              |")
    print ("| Title: nmap2spidery.py                                                                     |")
    print ("| Creation Date: 30/03/2020                                                                  |")
    print ("| Version Control: 1.0 - Draft Concept                                                       |")
    print ("| Description:                                                                               |")
    print ("| Ping and OS scan, chewed up and spat out in Spidery \'Source and Target Overview\' format.   |")
    print ("+--------------------------------------------------------------------------------------------+")

def usage():
    print ("Usage: " + sys.argv[0] + " -f <network ranges(s) input file> -o <output file> (default: \"spidery_goodness.txt\")")
    print (f"Example: {sys.argv[0]} -f network_ranges.txt -o spidery_goodness.txt")

## Main Class
def main (input, output):
    try:
        with open (input) as file:
            print (f"[+] Conducting reachability scan")
            networks = file.readlines()
            for network in networks:
                
                os.system("nmap -v0 -sn -iL " + input + " -oG reachable")                         
            print ("[+] Reachability scan complete")    
            
    except FileNotFoundError:
        print (f"[!] Error: No such file - \"{input}\"\n")

    results = "reachable"
    host_count = 0
    hosts = []

    ## Gathering total host counts
    try:
        with open (results) as file:
            data = file.readlines()
            for lines in data:
                if "Host" in lines:
                    hosts.append(lines.strip()[6:-14])
                    host_count += 1
    except FileNotFoundError:
        print (f"[!] Error: No such file - \"{results}\"\n")


    os_scan = []
    service_scan = []
    total_services = 0
    windows_systems = 0
    linux_systems = 0
    unix_systems = 0
    other_systems = 0

    ## Detecting OS's
    ## Detecting Services behind open ports
    print("[+] Fingerprinting host OS's")
    print("[+] SYN scanning for services")

    for host in hosts:
        service_scan = nm.nmap_syn_scan(host)
        os_scan = nmap.nmap_os_detection(host)
        
        for i in os_scan:
            if "linux" in (i["osclass"]["osfamily"]).lower():
                linux_systems += 1
            elif "windows" in (i["osclass"]["osfamily"]).lower():
                windows_systems += 1
            elif "unix" in (i["osclass"]["osfamily"]).lower():
                unix_systems += 1
            else:
                other_systems += 1
        
        for i in service_scan:
            if "open" in (i["state"].lower()):
                total_services += 1
                top_ports.append(i["port"])

    # print (top_ports)

    ## Conducting Service scan of reachable hosts
    print (f"[+] Writing output to {output}")
    print("\nOverview of the Source Network\n")
    print (f"\tLive Hosts: {host_count}")
    print (f"\tWindows Systems: {windows_systems}")
    print (f"\tLinux Systems: {linux_systems}")
    print (f"\tUnix Systems: {unix_systems}")
    print (f"\tOther Systems: {other_systems}")
    print(f"\nTotal count of accessible services: {total_services}")
    print(f"\nMost Popular Services (Top 10):\n")
    set_ports = set(top_ports)
    count = Counter(top_ports)
    for ports in sorted(set_ports):
        print (f"\tService {ports}/tcp: {count[ports]}")
    
    ## Write out file
    with open (output, "w") as file:
        file.write("Overview of the Source Network\n")
        file.write(f"\tLive Hosts: {host_count}\n")
        file.write(f"\tWindows Systems: {windows_systems}\n")
        file.write(f"\tLinux Systems: {linux_systems}\n")
        file.write(f"\tUnix Systems: {unix_systems}\n")
        file.write(f"\tOther Systems: {other_systems}\n")
        file.write(f"\nTotal count of accessible services: {total_services}\n")
        file.write(f"\nMost Popular Services (Top 10):\n")
        for ports in sorted(set_ports):
            file.write (f"\tService {ports}/tcp: {count[ports]}\n")

    ## Cleaning UP
    os.system('rm reachable')

if __name__=='__main__':
    banner()
    if len(sys.argv) <  2:
        usage()
    else:
        try:
            opts, args = getopt.gnu_getopt(sys.argv,"hf:o",["file=","output="])
            for opt, arg in opts:
                if opt == "-h":
                    usage()
                    sys.exit(2)
                elif opt in ("-f", "--ifile"):
                    input_file = sys.argv[2]
                elif opt in ("-o", "--output"):
                    output_file = sys.argv[4]
                else:
                    usage()
                    sys.exit(2)

            main(input_file, output_file)

        except getopt.GetoptError as err:
            print (err)
            usage()
            sys.exit(2)
        
