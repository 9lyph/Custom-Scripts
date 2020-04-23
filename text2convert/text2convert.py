#!/usr/bin/env python3

import sys
import os
import binascii
import getopt

def Banner():
    os.system('clear')
    print("+-------------------+")
    print(f"| \'{sys.argv[0]}\' |")
    print("| Author: " + "\u2141" + "lyph     |")
    print("+-------------------+")

def Usage():
    os.system('clear')
    print ("+------------------------------------------------------------------------------------------+")
    print ("| Takes a plaintext input and converts it according to the options specified as arguments. |")
    print (f"| {sys.argv[0]} -[dob] <plaintext to convert>\t\t\t\t\t\t   |")
    print (f"| Example 1: [+] {sys.argv[0]} -d \"string to convert\"\t\t\t\t\t   |")
    print (f"| Example 2: [+] {sys.argv[0]} -do \"string to convert\"\t\t\t\t   |")
    print (f"| Example 3: [+] {sys.argv[0]} -dob \"string to convert\"\t\t\t\t   |")
    print (f"| Example 4: [+] {sys.argv[0]} -dobx \"string to convert\"\t\t\t\t   |")
    print ("+------------------------------------------------------------------------------------------+")

def toDecimal(text):
    decimal = []
    [decimal.append(ord(i)) for i in text]
    print("\n[+] Decimal Output: ", end='', flush=True)
    [print (dec, end=' ', sep='', flush=True) for dec in decimal]

def toOctal(text):
    octal = []
    [octal.append(oct(ord(i))) for i in text]
    print("\n[+] Octal Output: ", end='', flush=True)
    [print (octalies[2:], end=' ', sep='', flush=True) for octalies in octal]

def toBinary(text):
    binary = []
    [binary.append(bin(ord(i))) for i in text]
    print("\n[+] Binary Output: ", end='', flush=True)
    for binaries in binary:
        if binaries == '0b100000':
            print ("00" + binaries[2:], end=' ', sep='', flush=True)
        else:
            print ("0" + binaries[2:], end=' ', sep='', flush=True)

def toHex(text):
    hexa = []
    [hexa.append(hex(ord(i))) for i in text]
    print ("\n[+] Hex Output: ", end='', flush=True)
    [print (hexies[2:], end=' ', sep='', flush=True) for hexies in hexa]



def Main():
    text = sys.argv[2]
    try:
        opts, args = getopt.gnu_getopt(sys.argv,"hdobx",["decimal=","octal=","binary=","hex="])
        for opt, arg in opts:
            if opt == "-h":
                Usage()
                sys.exit()
            elif opt in ("-d", "--decimal"):
                toDecimal(text)
            elif opt in ("-o", "--octal"):
                toOctal(text)
            elif opt in ("-b", "--binary"):
                toBinary(text)
            elif opt in ("-x", "--hex"):
                toHex(text)
            else:
                Usage()
                sys.exit()

    except getopt.GetoptError as err:
        print (err)
        Usage()
        sys.exit(2)

if __name__ == '__main__':
    if len(sys.argv) <  3:
        Usage()
    else:
        Banner()
        Main()
        