# ⅁lyph's Custom Scripts

This repo contains various scripts including:

- NMAP to excel converter (GNMAP to XLS).  Currently supports GNMAP format. Takes the output of a Greppable NMAP scan results, filtered on                OPEN ports per IP/Node, and then populates an excel spreadsheet with the findings.  Incorporating Styles Headings and Sheets where required.
- Native Server/Client Python Reverse Shell Implementation
- A simple TCP Server and associated TCP Client.
- IP Address To Binary Notation Converter.
- Host list to Port Status.  Allows input list of host(s) and conducts a scan for given open ports.
- Quick and dirty TCP Active Port Scanner
- Urlscraper. Simple Scraper to listout all HREF's within a choosen domain.
- FTP Brute Forcer. Simple FTP brute force util.

### Installation - nmap2excel.py/nmap2excel.exe

Clone this repository and run as required and as per usage below.

### Usage

    nmap2excel.py -i file -o file -t [output input file contents to terminal]
    nmap2excel.exe -i file -o file -t [outputs input file contents to terminal]
    -i .gnmap format file
    -o filename of your chosen output file (appends .xls)
    -t terminal output

### Installation - SimpleServer.py

Clone this repository and run as required and as per usage below.

### Usage

    SimpleServer.py <host> <port>
    host - chosen server IP address
    port - chosen listening port

### Installation - SimpleClient.py 

Clone this repository and run as required and as per usage below.
    
### Usage

    SimpleClient.py <host> <port>
    host - server IP address to connect to
    port - server port to connect to
   
### Installation - server2shell.py

Clone this repository and run as required and as per usage below.

### Usage

    server2shell.py -t <bind address> -p <bind port>
    <bind address> - server IP address to bind to, in order to allow a client to connect
    <bind port> - server port to bind to, in order to allow a client to connect

### Installation - client2shell.py

Clone this repository and run as required and as per usage below.

### Usage

    client2shell.py -t <target host> -p <target port>
    <target address> - server IP address to connect to
    <target port> - server port to connect to
    
### Installation - ip2binary.py/ip2binary.exe

Clone this repository and run as required and as per usage below.

### Usage

    ip2binary.py <ip_address to be converted>
    ip2binary.exe <ip_address to be converted>
    <ip_address to be converted> - Requires a valid IP address in dot notation e.g. 1.1.1.1

### Installation - host2port.py

Clone this repository and run as required and as per usage below.

### Usage

    host2port.py -i <host file> -p <port(s)>
    <host file> - list of hosts (can be based on an output from sublist3r for instance)
    <port(s)> - comma separated ports to scan against

### Example

    host2port.py -i 10.10.10.10 -p 21,22,80
    
### Installation - port2scan.py

Clone this repository and run as required and as per usage below.

### Usage

    port2scan.py <host> [<ports seperated by spaces>]

### Example

    port2scan.py www.google.com 21 22 80

### Installation - url2scraper.py

Clone this repository and run as required and as per usage below.

### Usage

    url2scraper.py -i <host file> -o <output file> -t <pipes output to terminal>
    NOTE: -o and -t: Optional

### Example

    url2scraper.py -i hosts.txt -o somefile.txt -t

### Installation - ftp2brute.py

Clone this repository and run as required.

pip install -r requirements.txt

### Usage

    ftp2brute.py <host> <user> <wordlist>
    Default port in use 'tcp/21'

### Example
    
    ftp2brute.py 192.168.1.1 root wordlist.txt
