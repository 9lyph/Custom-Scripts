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
    newHex = ""
    [hex.append(i) for i in input]
    x = 0
    print ("[+] Converting ...")
    for i in hex:
        try:
            newHex+=("\\x"+hex[x].lower()+hex[x+1].lower())
            # print ("\\x" + hex[x].lower()+hex[x+1].lower(), flush=True, end='')
            x+=2
        except IndexError:
            pass
    print (newHex)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        main()