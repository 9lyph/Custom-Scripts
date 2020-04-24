#!/usr/bin/env python3
import binascii
import sys
from sys import stdout
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-x', '--hex', action='store', dest='x', help='Hex that you would like to convert to ascii', default='')
parser.add_argument('-a',  '--ascii', action='store', dest='a', help='Ascii that you would like to convert to hex', default='')
args = parser.parse_args()

def Banner():
    os.system('clear')
    print ("+==================================================================================================================================================")
    print ("|")
    print ("| Title: %s" % sys.argv[0])
    print ("| Author: glyph")
    print ("| Creation Date: 21/02/2020")
    print (f"| Usage: {sys.argv[0]} '-x' \'<hex to convert to ascii>\' OR {sys.argv[0]} -a' \'<ascii to convert to hex>\'")
    print ("| Description: This takes either a ASCII string or HEX Value set, with the opposite result as output.")
    print ("|")
    print ("+==================================================================================================================================================")

def Usage():
    print (f"Usage: {sys.argv[0]} '-x' \'<hex to convert to ascii>\' OR {sys.argv[0]} -a' \'<ascii to convert to hex>\'")

def asciiPrint(string):
    hexarray = []
    print ("[Original String]\n\n\'%s\'" % string)
    for char in string:
        y = binascii.hexlify(bytearray(char, 'utf-8'))
        hexarray.append(y)

    print ("\n[Hex Conversion]\n") 
    for i in hexarray:
        print ("\\x" + i.decode('utf-8'), end='')
    print ("\n")

def hexPrint(string):
    hexarray = []
    split = []
    if string[0:2] == "\\x":
        split = string.split("\\x")
    elif string[2] == " ":
        split = string.split(" ")
    else:
        i = 0
        string_spaced = ''
        for char in string:
            string_spaced += string[i:i+2] + " "
            i += 1
        split = string.split(" ")
            
    for char in split:
        if char == '':
            pass
        else:
            y = binascii.unhexlify(char)
            hexarray.append(y)

    print ("[Original Hex]\n\n\'%s\'" % string)
    print ("\n[Ascii Conversion]\n")
    for i in hexarray:
        print (i.decode('utf-8'), end='')
    print ("\n")

if __name__ == "__main__":
    Banner()
    if (args.x and args.a):
        Usage()
    elif args.x:
        hexPrint(args.x)
    elif args.a:
        asciiPrint(args.a)
