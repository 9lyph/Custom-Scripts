<p align="center">
<img src="images/glyph.jpg" width="250"/>
</p>

### This repo contains various scripts including:

- **nmap2excel.py** - namp to excel converter (gnmap to .xls).  Currently supports **gnmap** format. Takes the output of a Greppable NMAP scan results, filtered on                OPEN ports per IP/Node, and then populates an excel spreadsheet with the findings.  Incorporating Styles Headings and Sheets where required.
- **SimpleServer.py/SimpleClient.py** - simple TCP Server and associated TCP Client.
- **server2shell.py/client2shell.py** - native server/client python reverse shell implementation
- **ip2binary.py** - ip address to binary notation converter.
- **port2scan.py** - quick and dirty tcp active port scanner
- **url2scraper.py** - urlscraper. Simple scraper to listout all HREF's within a choosen domain.
- **ftp2brute.py** - ftp brute forcer. Simple ftp brute force utility.
- **ascii2hex.py** - ascii string to hex converter.
- **csrf2html.py** - csrf to html generator.  This allows input of a poc http GET/POST request as input with the resulting output being a poc html payload.
- **atbash2decrypt** - This script takes an 'atbash cipher' encrypted base64 string, whose output is original clear text
- **weather.py** - Pulls stats from Open Weather Map

### Installation - nmap2excel.py

Download available at the following location: [nmap2excel](https://github.com/9lyph/Custom-Scripts/blob/master/nmap2excel/nmap2excel.py)

### Usage

    nmap2excel.py -i file -o file -t [output input file contents to terminal]
    -i .gnmap format file
    -o filename of your chosen output file (appends .xls)
    -t terminal output

### Installation - SimpleServer.py

Download available at the following location: [SimpleServer](https://github.com/9lyph/Custom-Scripts/tree/master/Simple%20Python%20Server%20Client/SimpleServer.py)

### Usage

    SimpleServer.py <host> <port>
    host - chosen server IP address
    port - chosen listening port

### Installation - SimpleClient.py 

Download available at the following location: [SimpleClient](https://github.com/9lyph/Custom-Scripts/tree/master/Simple%20Python%20Server%20Client/SimpleClient.py)
    
### Usage

    SimpleClient.py <host> <port>
    host - server IP address to connect to
    port - server port to connect to
   
### Installation - server2shell.py

Download available at the following location: [Server2Shell](https://github.com/9lyph/Custom-Scripts/blob/master/server2shell/server2shell.py)

### Usage

    server2shell.py -t <bind address> -p <bind port>
    <bind address> - server IP address to bind to, in order to allow a client to connect
    <bind port> - server port to bind to, in order to allow a client to connect

### Installation - client2shell.py

Download available at the following location: [Client2Shell](https://github.com/9lyph/Custom-Scripts/blob/master/server2shell/client2shell.py)

### Usage

    client2shell.py -t <target host> -p <target port>
    <target address> - server IP address to connect to
    <target port> - server port to connect to
    
### Installation - ip2binary.py

Download available at the following location: [ip2binary](https://github.com/9lyph/Custom-Scripts/blob/master/ip2binary/ip2binary.py)

### Usage

    ip2binary.py <ip_address to be converted>
    ip2binary.exe <ip_address to be converted>
    <ip_address to be converted> - Requires a valid IP address in dot notation e.g. 1.1.1.1
    
### Installation - port2scan.py

Download available at the following location: [port2scan](https://github.com/9lyph/Custom-Scripts/blob/master/port2scan/port2scan.py)

### Usage

    port2scan.py <host> [<ports seperated by spaces>]

### Example

    port2scan.py www.google.com 21 22 80

### Installation - url2scraper.py

Download available at the following location: [url2scraper](https://github.com/9lyph/Custom-Scripts/blob/master/url2scraper/url2scraper.py)

### Usage

    url2scraper.py -i <host file> -o <output file> -t <pipes output to terminal>
    NOTE: -o and -t: Optional

### Example

    url2scraper.py -i hosts.txt -o somefile.txt -t

### Installation - ftp2brute.py

Download available at the following location: [ftp2brute](https://github.com/9lyph/Custom-Scripts/blob/master/ftp2brute/ftp2brute.py)

pip install -r requirements.txt

### Usage

    ftp2brute.py <host> <user> <wordlist>
    Default port in use 'tcp/21'

### Example
    
    ftp2brute.py 192.168.1.1 root wordlist.txt

### Installation - ascii2hex.py

Download available at the following location: [ascii2hex](https://github.com/9lyph/Custom-Scripts/blob/master/ascii2hex/ascii2hex.py)

### Usage

    ascii2hex.py -x '<string>'

### Example
    
    ascii2hex.py -a "Glyph"
    
### Installation - csrf2html.py

Download available at the following location: [csrf2html](https://github.com/9lyph/Custom-Scripts/blob/master/csrf2html/csrf2html.py)

### Usage

    csrf2html.py '<POC Request Filename>'

### Example
    
    csrf2html.py poc.txt

### Installation - atbash2decrypt.py

Download available at the following location: [atbash2decrypt](https://github.com/9lyph/Custom-Scripts/blob/master/atbash2decrypt/atbash2decrypt.py)

### Usage

    atbash2decrypt.py '<base64 encrypted text>'

### Example

    atbash2decrypt.py "FTV1MCxdxnJ="

### Installation - weather.py

Download available at the following location: [weather](https://github.com/9lyph/Custom-Scripts/blob/master/weather/weather.py)

### Usage

    weather.py

### Example

    weather.py
