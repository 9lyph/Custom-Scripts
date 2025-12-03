<p align="center">
<img src="images/9lpyh-new.jpg" width="250"/>
</p>

### This repo contains various scripts including:

- **nmap2excel.py** - nmap to excel converter (gnmap to .xls).  Currently supports **gnmap** format. Takes the output of a Greppable NMAP scan results, filtered on                OPEN ports per IP/Node, and then populates an excel spreadsheet with the findings.  Incorporating Styles Headings and Sheets where required.
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
- **text2convert.py** - Converts plaintext input to Dec, Octal, Binary, Hex output
- **ping2sweep.py** - Performs a PING sweep given an IP Range
- **crackitycrack.sh** - Bash Shell MD5 cracker
- **hexBytes** - Produces a list of all hex characters, in hex format
- **raw2hex** - Takes raw hex e.g. aabbcc and outputs in curated format e.g. \xaa\xbb\xcc
- **scraper.py** - Basic Web Site Crawler and scraper of information

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

### Installation - text2convert.py

Download available at the following location: [text2convert](https://github.com/9lyph/Custom-Scripts/blob/master/text2convert/text2convert.py)

### Usage

    text2convert.py -[dobx] "<string to convert>"

### Example

    Example 1: [+] text2convert.py -d "string to convert"
    Example 2: [+] text2convert.py -do "string to convert"
    Example 3: [+] text2convert.py -dob "string to convert"
    Example 4: [+] text2convert.py -dobx "string to convert"
    
### Installation - ping2sweep.py

Download available at the following location: [ping2sweep](https://github.com/9lyph/Custom-Scripts/tree/master/ping2sweep/ping2sweep.py)

### Usage

    ping2sweep <IPAddress Range> [-o] <optional output file> 

### Example

    ping2sweep 192.168.1.0/24 -o sweep.txt

### Output Format

```
    +-------------------+
    | 'ping2sweep.py'   |
    | Author: ⅁lyph     |
    +-------------------+
    [+] Sweeping host(s) 192.168.1.0/24 ...
    [-] Host: 192.168.1.0 unreachable
    [+] Host: 192.168.1.1 reachable
```

### Installation - crackitycrack.sh

Download shell script and run accordingly

### Usage
    
    crackitycrack.sh <hash> <wordlist>

### Example

    ./crackitycrack.sh 26323c16d5f4dabff3bb136f2460a943 wordlist.txt

### Output Format

    Trying:  qazwsx
    +
    | Cracked Hash:  26323c16d5f4dabff3bb136f2460a943
    | Cleartext   :  onceuponatime
    +

### Installation - hexBytes.py

Just run the script

### Example
 
    ./hexBytes.py

### Output Format 

    badchars=
    ("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")
    ("\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f")
    ("\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f")
    ("\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f")
    ("\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f")
    ("\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f")
    ("\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f")
    ("\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f")
    ("\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f")
    ("\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f")
    ("\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf")
    ("\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf")
    ("\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf")
    ("\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf")
    ("\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef")
    ("\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
    
### Installation - raw2hex.py

Download available at the following location: [raw2hex](https://github.com/9lyph/Custom-Scripts/tree/master/raw2hex/raw2hex.py)

### Usage
 
    ./raw2hex.py aabbcc

### Output Format

    [+] Converted: \xaa\xbb\xcc

### Installation - scraper.py

Requires BeautifulSoup Module

Download available at the following location: [scraper](https://github.com/9lyph/Custom-Scripts/tree/master/scraper/scraper.py)

### Usage
 
    ./scraper.py [-h] [--delay DELAY] [--max-pages MAX_PAGES] url

### Output Format

    [INFO: Scraping: https://exploitsecurity.io

    ============================================================
    SCRAPING RESULTS FOR: https://exploitsecurity.io
    ============================================================
    Company Name: Exploit Security
    
    Emails Found (15):
       • 18d2f96d279149989b95faf0a4b41882@sentry-next.wixpress.com
       • 2062d0a4929b45348643784b5cb39c36@sentry.wixpress.com
       • 271e9fa3230b4eec94b02bf95780f5f2@sentry.wixpress.com
       • 460ff4620fa44cba8df530afde949785@sentry.wixpress.com
       • 5d1795a2db124a268f1e1bd88f503500@sentry.wixpress.com
       • 605a7baede844d278b89dc95ae0a9123@sentry-next.wixpress.com
       • 78f7996315bc402f9dcb8a2f974b82d1@sentry.wixpress.com
       • 8c4075d5481d476e945486754f783364@sentry.io
       • 98b21aa53d68482b8414e892d9af0e5f@sentry-next.wixpress.com
       • 9a65e97ebe8141fca0c4fd686f70996b@sentry.wixpress.com
       • bfb679c754744c58a7374ee6e25cfc13@sentry.wixpress.com
       • c183baa23371454f99f417f6616b724d@sentry.wixpress.com
       • dd0a55ccb8124b9c9d938e3acf41f8aa@sentry.wixpress.com
       • ed436f5053144538958ad06a5005e99a@sentry.wixpress.com
       • info@exploitsecurity.io
    
    Phone Numbers (2):
       • 1800 252 919
       • 670304435
    
    Social Media:
       • Linkedin: exploitsecurityio
       • Twitter: bt
       • Twitter: 3xploit5ecurit7
       • Twitter: suricate
       • Twitter: bolt
    
    Possible Addresses:
       • Damn Vulnerable Raspberry Pi
       • Our Security Research Services are highly sought after and comprise of deep diving into hardware and applications
       • Our expert team is committed to providing you with the most thorough, proactive, and effective penetration testing solutions. We ensure that your systems remain resilient to emerging threats, empowering you to mitigate risks and achieve robust security compliance.
       • Each of these services is performed by our highly skilled and certified penetration testers, who employ the latest tools, methodologies, and industry best practices to uncover hidden threats. By partnering with us, you gain actionable insights that not only enhance the security of your digital and physical infrastructure but also safeguard your organization's reputation, assets, and operations.
       • Exploit Security was established to offer security consultancy through a connected group of white hat freelancers.  Based in Sydney, Australia, our team of passionate white hat security researchers are dedicated to the breaking of our clients target systems so that black hats don't get the chance to. Security research is at the heart of our business and with a specialty for embedded systems and IoT we endeavour to use this expertise to help our clients fortify their systems before being made a target of compromise themselves.
       • directly targeted to tease out vulnerabilities from.
       • Don't have a penetration testing practise ? We can help by taking on that function for you. Using our skilled team of Penetration Testers and Security Researchers, we are able to take on the task with agility and professionalism.
       • Our Penetration Testing Sydney services provide organizations with unparalleled visibility into their security posture, enabling proactive identification and remediation of vulnerabilities before they can be exploited. Through rigorous and detailed testing of critical systems, we empower our clients to strengthen their defenses against evolving cyber threats.
       • challenges that include concepts found within Hardware Hacking, Embedded Systems and IoT.
    
    Pages crawled: 1
    ============================================================
    
    Emails saved to scraped_emails.txt


#### Follow me on
[Mastodon](https://defcon.social/@9lyph) [Linkedin](https://www.linkedin.com/in/victor-h-a894a84/) [Youtube](https://www.youtube.com/channel/UC79Q2b0tHeqsjjvEH0k7jZw)
