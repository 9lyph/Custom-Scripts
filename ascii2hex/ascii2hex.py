import binascii
import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-x', '--hex', action='store', dest='x', help='Hex that you would like to convert to ascii', default='')
parser.add_argument('-a',  '--ascii', action='store', dest='a', help='Ascii that you would like to convert to hex', default='')
args = parser.parse_args()

# def getArgument(args):
#     switch = {
#         'a':asciiPrint(args.a),
#         'x':hexPrint(args.x)
#     }

def Banner():
    os.system('clear')
    print ("+==================================================================================================================================================")
    print ("|")
    print ("| Title: %s" % sys.argv[0])
    print ("| Author: Glyph")
    print ("| Usage: %s \'<string>\' \'-x\' <hex to convert to ascii> OR %s \'<string>\' \'-a\' <ascii to convert to hex>") % (sys.argv[0], sys.argv[0])
    print ("| Summary: Converts either an input ascii string to hexadecimal OR hexadecimal string to ascii")
    print ("|")
    print ("+==================================================================================================================================================")

def Usage():
    print ("Usage: %s \'<string>\' '-x' <hex to convert to ascii> OR %s \'<string>\' -a' <ascii to convert to hex>") % (sys.argv[0], sys.argv[0] )

def asciiPrint(string):
    hexarray = []
    print ("[Original String]\n\n\'%s\'" % string)
    for char in string:
        y = str(binascii.hexlify(char))
        hexarray.append(y)

    print ("\n[Hex Conversion]\n")   
    for i in hexarray:
        print("\\x%s" %i),

def hexPrint(string):
    joined = string.replace(" ", "")
    split = joined.split("\\x")
    print split
    # for char in string:
    #     print char,
    # joined = hex(string.replace(" ", ""))

    # hexarray = []
    # print ("[+] Original String:\n%s\n" % string)
    # for char in string:
    #     y = str(binascii.hexlify(char))
    #     hexarray.append(y)

    # print ("[+] Hexed:")
    # for i in hexarray:
    #     print("\\x%s" %i),
    # print ("\n")

if __name__ == "__main__":
    Banner()
    if (args.x and args.a):
        Usage()
    elif args.x:
        hexPrint(args.x)
    elif args.a:
        asciiPrint(args.a)