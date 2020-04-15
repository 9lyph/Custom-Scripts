#!/usr/bin/env python3

import sys
import requests
import json
import os



def banner():
    os.system('clear')
    print("+---------------+")
    print("| \'The Weather\' |")
    print("| Author: " + "\u2141" + "lyph |")
    print("+---------------+")

def main():
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    headers = { 'X-RapidAPI-Host':'community-open-weather-map.p.rapidapi.com',
                'X-RapidAPI-Key': '09bb8fd4a7msh36e40cae1db3fb4p11e9b6jsnbdde1dc164f2'
    }

    params = { "q":"sydney,036","units":"metric","lang":"en","id":"Sydney" }

    r = requests.get(url, headers=headers, params=params)
    json_object = json.loads(r.text)

    list1 = (json_object)['list']
    dictionary = list1[0]

    dt      = (dictionary['dt'])       # type int
    main    = (dictionary['main'])     # type dictionary
    weather = (dictionary['weather'])  # type list
    clouds  = (dictionary['clouds'])   # type dictionary
    wind    = (dictionary['wind'])     # type dictionary
    sys     = (dictionary['sys'])      # type dictionary
    dt_txt  = (dictionary['dt_txt'])   # type string
    city    = (json_object['city']['name'])
    print ("+---------------+")
    print (f"| City: {city}\t|" )
    print ("+---------------+")
    print ("+------------------------------------+")
    print ("|\t\t\t\t     |")
    print ("| Details\t\t\t     |")
    print ("|\t\t\t\t     |")

    for k,v in main.items():
        print (f"| {k}: \t{v}\t\t     |")

    for i in weather:
        print (f"| Description:\t{i['main']}\t\t     |")
        print (f"|\t\t{i['description']}     |")
        print ("|\t\t\t\t     |")
        print ("+------------------------------------+")

if (__name__ == '__main__'):
    banner()
    main()