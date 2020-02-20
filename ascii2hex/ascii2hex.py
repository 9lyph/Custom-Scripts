import binascii
import sys
import os

def Banner():
    os.system('clear')
    print ("+=========================================================================")
    print ("|")
    print ("| Title: %s" % sys.argv[0])
    print ("| Author: Glyph")
    print ("| Usage: %s \'<string>\'" % sys.argv[0])
    print ("| Summary: Converts an input ascii string to hexidecimal")
    print ("|")
    print ("+=========================================================================")

def Usage():
    print ("Usage: %s \'<string>\'" % sys.argv[0])

def Main(string):
    hexarray = []
    print ("[+] Original String:\n%s\n" % string)
    for char in string:
        y = str(binascii.hexlify(char))
        hexarray.append(y)

    print ("[+] Hexed:")
    for i in hexarray:
        print("\\x%s" %i),
    print ("\n")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        Banner()
        Main(str(sys.argv[1]))
    else:
        Usage()
        sys.exit()
