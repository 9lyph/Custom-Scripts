# Glyph Custom Repo

Author: Glyph

Initial Date of Creation: 23/01/2018

This repo contains various projects.

1. SimpleServer.py - This is a very simple TCP server, invoked using two arguments.
  Usage: SimpleServer.py \<host\> \<port\>
2. SimpleClient.py - This is a very simple TCP client, which can be used to connect using a specified Host and Port. 
  Usage: SimpleClient.py \<host\> \<port\>
3. nmap2excel/* - NMAP to excel converter (GNMAP to XLS).  Currently supports GNMAP format. Takes the output of a Greppable NMAP scan results, filtered on OPEN ports per IP/Node, and then populates an excel spreadsheet with the findings.  Incorporating Styles Headings and Sheets where required.
  Usage: nmap2excel.py -i file -o file -t [outputs input file contents to terminal]
  a. nmap2excel.exe - PE for 64 bit windows
