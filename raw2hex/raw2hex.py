#!/usr/bin/env python3

import sys
import binascii
import base64
import os

def usage():
    os.system('clear')
    print (f"[+] Usage: {sys.argv[0]} <raw hex here>")

def main():
    os.system('clear')
    input = sys.argv[1]
    hex = []
    [hex.append(i) for i in input]
    x = 0
    print ("[+] Converted:")
    for i in hex:
        try:
            print ("\\x" + hex[x].lower()+hex[x+1].lower(), flush=True, end='')
            # sys.stdout.flush()
            x+=1
        except IndexError:
            pass

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        main()