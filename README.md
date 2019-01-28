# Glyph Custom Repo

Author: Glyph

Initial Date of Creation: 23/01/2018

This repo contains various projects.

1. SimpleServer.py - This is a very simple TCP server, invoked using two arguments.
  Usage: SimpleServer.py \<host\> \<port\>
2. SimpleClient.py - This is a very simple TCP client, which can be used to connect using a specified Host and Port. 
  Usage: SimpleClient.py \<host\> \<port\>
3. nmap2excel.py - The idea behind this concept is to take the output of a Greppable NMAP scan, filter on OPEN ports per IP/Node,
and populate an excel spreadsheet with the findings.  Incorporating Styles Headings and Sheets where required.
  Usage: nmap2excel.py -i file -o file -t [outputs input file contents to terminal]
