Overview

nmap2excel.py - Python script that Converts .gnmap to excel .xls
nmap2excel.exe - Windows PE that converts .gnmp to excel .xls

    NMAP to excel converter (GNMAP to XLS).  Currently supports GNMAP format. Takes the output of a Greppable NMAP scan results, filtered on                OPEN ports per IP/Node, and then populates an excel spreadsheet with the findings.  Incorporating Styles Headings and Sheets where required.

Installation

    Clone this repository.

Usage

    nmap2excel.py -i file -o file -t [outputs input file contents to terminal]
    -i .gnmap format file
    -o filename of your chosen output file (appends .xls)
    -t terminal output

SimpleServer.py - This is a very simple TCP server, invoked using two arguments.

Installation

    Clone this repository.

Usage

    SimpleServer.py <host> <port>
    host - chosen server IP address
    port - chosen listening port

SimpleClient.py - This is a very simple TCP client, which can be used to connect using a specified Host and Port. 

Installation

    Clone this repository
    
Usage

    SimpleClient.py <host> <port>
    host - server IP address to connect to
    port - server port to connect to
   
