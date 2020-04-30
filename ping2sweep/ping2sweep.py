import os
import sys
import os.path
import ipaddress
import platform

def Banner():
    os.system('clear')
    print("+-------------------+")
    print(f"| \'{sys.argv[0]}\'   |")
    print("| Author: " + "\u2141" + "lyph     |")
    print("+-------------------+")

def Usage():
    print ("+-------------------------------------------------------+")
    print ("| Ping sweep with given input of 'IPAddress/CIDR'       |")
    print ("|\t\t\t\t\t\t\t|")
    print (f"| {sys.argv[0]} <IPAddress/CIDR>\t\t        |")
    print ("|\t\t\t\t\t\t\t|")
    print(f"| Example: {sys.argv[0]} 192.168.1.0/29\t\t\t|")
    print ("+-------------------------------------------------------+")

def cleanUp():
    if os.path.isfile("sweep.txt"):
        os.system('rm sweep.txt')
    else:
        sys.exit()

def Main(argv):
    ip_address = str(argv[0])
    raw_ip_address = str(argv[0][:-3])
    mask = ip_address.split('/')[1]
    with open ("sweep.txt", "w") as f:
        try:
            print (f"[+] Sweeping host(s) {sys.argv[1]} ...")
            for addr in ipaddress.IPv4Network(raw_ip_address+"/"+mask):
                if (platform.system() == 'Darwin'):
                    result = os.system("ping -c 1 -W 100 " + str(addr) + " 1>/dev/null")
                elif (platform.system() == 'Linux'):
                    result = os.system("ping -c 1 -w 100 " + str(addr) + " 1>/dev/null")
                if result == 512:
                    f.write(F"[-] Host: {str(addr)} unreachable\n")
                else:
                    f.write(f"[+] Host: {str(addr)} reachable\n")
        except ValueError as err:
            print (err)

    with  open ("sweep.txt", "r") as f:     
        for line in f.readlines():
            print (line, end='', flush=True)

if __name__ == '__main__':
    Banner()
    if len(sys.argv) < 2:
        Usage()
    else:
        Main(sys.argv[1:])
        cleanUp()



