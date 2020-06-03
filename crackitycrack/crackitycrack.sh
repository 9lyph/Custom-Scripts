#!/bin/bash
clear
if [ $# -lt 2 ]; then
    echo "+======================================================+"
    echo "| Author: glyph                                        |"
    echo "| Usage: " $0 "<MD5 hash> <wordlist>     |"
    echo "+======================================================+"
    exit 1
fi
toMatch=$1
wordlist=$2
for i in $(cat $2); do
    STUFF=`echo -n $i | openssl md5`
    if [ $STUFF == $toMatch ]; then
        echo "+"
        echo "| Cracked Hash: " $STUFF
        echo "| Cleartext   : " $i
        echo "+"
        break
    else
        echo "Trying: " $i
    fi
done;
