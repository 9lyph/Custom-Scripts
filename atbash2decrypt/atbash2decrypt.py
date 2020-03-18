#!/usr/bin/env python3

import sys
import numbers
import base64
import os

encoded = []
upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = list("abcdefghijklmnopqrstuvwxyz")

indexing = {\
    0:"Z",\
    1:"Y",\
    2:"X",\
    3:"W",\
    4:"V",\
    5:"U",\
    6:"T",\
    7:"S",\
    8:"R",\
    9:"Q",\
    10:"P",\
    11:"O",\
    12:"N",\
    13:"M",\
    14:"L",\
    15:"K",\
    16:"J",\
    17:"I",\
    18:"H",\
    19:"G",\
    20:"F",\
    21:"E",\
    22:"D",\
    23:"C",\
    24:"B",\
    25:"A"}    

def Banner():
    os.system('clear')
    print ("+------------------------------------------------------------------------------------------------------------------+")
    print ("| Author: glyph                                                                                                    |")
    print ("| Title: atbash2decrypt.py                                                                                         |")
    print ("| Version Control: 1.0 - Draft Concept                                                                             |")
    print ("| Description: This script takes an \'atbash cipher\' encrypted base64 string whose output original clear text.    |")
    print ("| Usage: " + sys.argv[0] + "\'<base64 encrypted text>\'" + "\t\t                                                   |")
    print ("+------------------------------------------------------------------------------------------------------------------+")

def Usage():
    print ("\nUsage: " + sys.argv[0] + " \'<base64 encrypted text>\'" )

def Main():
    string = list(sys.argv[1])
    for i in string:
        if (i.isdigit()):
            encoded.append(i)
        elif (i.isupper()):
            encoded.append(indexing.get(int(upper.index(i))))
        elif (i.islower()):
            encoded.append(indexing.get(int(lower.index(i))).lower())
        elif (i == '=' or i == '+'):
            encoded.append(i)
        else:
            pass

    print ("[+]----------------------------------")
    print ("[+] Decrypted: " + base64.b64decode(''.join(encoded)).decode('utf-8'))
    print ("[+]----------------------------------")

if (__name__ == "__main__"):
    if (len(sys.argv) > 1):
        Banner()
        Main()
    else:
        Usage()

