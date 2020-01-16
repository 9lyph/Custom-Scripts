#!c:\Python27\python.exe
# -*- coding: UTF-8 -*-

'''
Author: ⅁lyph
Title: nmap2excel.py
Creation Date: 24/01/2018
Version Control: 1.0 - Draft Concept
Description: The idea behind this concept is to take the output of a PCI NMAP, filter on OPEN ports per IP/Node,
and populate an excel spreadsheet with the findings.  Incorporating Styles Headings and Sheets 
where required.

'xlwt' library installation steps
=================================
1. pip install xlwt

Script Usage
============

Usage: nmap2excel.py -i file -o file -t [outputs input file contents to terminal]
Options:
-i Input file: The name/path to the resultant nmap file (Currently functioning using a .gnmap extention, with view to further this in future)
-o Output file: The name/path of the excel file for production (Defaults to .xlsx)
-t Output to Terminal: This outputs contents of input file to the terminal
'''

import sys
import os
import openpyxl
import getopt
import time
import xlwt

def initialiseVariables():
	global format_file
	format_file = []
	global input_file
	input_file = []
	global output_file
	output_file = ""
	global hosts
	hosts = {}
	global message
	message="......"

def banner():
	os.system('cls')
	print (" _   _ __  __          _____ ___  ________   _______ ______ _      ")
	print ("| \ | |  \/  |   /\   |  __ \__ \|  ____\ \ / / ____|  ____| |     ")
	print ("|  \| | \  / |  /  \  | |__) | ) | |__   \ V / |    | |__  | |     ")
	print ("| . ` | |\/| | / /\ \ |  ___/ / /|  __|   > <| |    |  __| | |     ")
	print ("| |\  | |  | |/ ____ \| |    / /_| |____ / . \ |____| |____| |____ ")
	print ("|_| \_|_|  |_/_/    \_\_|   |____|______/_/ \_\_____|______|______|\n")
	print ("-------------------------------------------------------------------------------------------------------------------|")
	print ("| Author: glyph                                                                                                    |")
	print ("| Title: nmap2excel.py                                                                                             |") 
	print ("| Creation Date: 24/01/2018                                                                                        |")
	print ("| Version Control: 1.0 - Draft Concept                                                                             |") 
	print ("| Description: The idea behind this concept is to take the output of a PCI NMAP, filter on OPEN ports per IP/Node, |")
	print ("| and populate an excel spreadsheet with the findings.  Incorporating Styles Headings and Sheets                   |") 
	print ("| where required.                                                                                                  |")
	print ("-------------------------------------------------------------------------------------------------------------------|")

def snoozing():
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep (0.2)

def readFile(arg):
	with open(sys.argv[2]) as file:
    		for line in file: 
    			line = line.strip()
        		input_file.append(line)

        print ("\nReading input file \'" + str(sys.argv[2] + "\'"))
        snoozing()
        return(input_file)
    
def writeFile(arg):
	loadingDictionary()
	if arg[-4:] == '.xls':
		print ("\nWriting output file: " + arg)
		snoozing()
		writeExcel()
	else:	
		print ("\nWriting output file: " + arg + ".xls")
		snoozing()
		writeExcel()
	print ("\nWrite Complete!")

def writeExcel():
	# Declaring Styles
	style0 = xlwt.easyxf('font: name Calibri, color-index black, bold on')
	style1 = xlwt.easyxf('font: name Calibri, color-index black, bold off')

	#Declaring Workbook and Worksheet objects
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Results', cell_overwrite_ok=True)

	#Writing default headers and Sheet Title
	ws.write(0, 0, 'Host', style0)
	ws.write(0, 1, 'Ports', style0)

	#Writing blank line
	ws.write(1, 0, '', style1)
	ws.write(1, 1, '', style1)
	ws.write(1, 2, '', style1)

	row=2
	col=0
	for list_item in input_file:
		if 'Host:' in list_item:
			if not 'Status' in list_item:
				format_file = list_item.split(" ")
				host = str(format_file[1])
				ws.write(row, col, host, style1)
				for i in range (len(format_file[3:-3])):
		 			port = str(format_file[3:-3][i].split("/")[0])
		 			hosts = {host:port}
		 			ws.write(row, col + 1, port, style1)
		 			row+=1

	wb.save(sys.argv[4]+".xls")

def loadingDictionary():
	for list_item in input_file:
		if 'Host:' in list_item:
			if not 'Status' in list_item:
				format_file = list_item.split(" ")
				host = str(format_file[1])
				for i in range (len(format_file[3:-3])):
		 			port = str(format_file[3:-3][i].split("/")[0])
		 			hosts = {host:port}
					
def outputtoConsole(arg):
	print ("\nOutputting contents of \'" + sys.argv[2] + "\' to terminal")
	snoozing()
	terminal()

def usage():
	print ("Usage: " + sys.argv[0][-13:] + " -i <input file> -o <output file> -t [outputs input file contents to terminal]")
	
def terminal():
	#Here we are trying to format out unwanted '.gnmap' lines
	for list_item in input_file:
		if 'Host:' in list_item:
			if not 'Status' in list_item:
				format_file = list_item.split(" ")
				host = str(format_file[1])
				print ("\n[Host]\n" + "+-" + host)
				for i in range (len(format_file[3:-3])):
		 			port = str(format_file[3:-3][i].split("/")[0])
		 			hosts = {host:port}
					print ("+-[Ports]" + " " + port)

def main(argv):
	initialiseVariables()
	banner()
	try:
		opts, args = getopt.gnu_getopt(argv,"hio:t",["ifile=","ofile=","terminal="])
	except getopt.GetoptError as err:
		print (err)
		usage()
		sys.exit(2)
   	for opt, arg in opts:
		if opt == "-h":
			usage()
			sys.exit()
		elif opt in ("-i", "--ifile"):
			input_file = readFile(arg)
		elif opt in ("-o", "--ofile"):
			writeFile(arg)
		elif opt in ("-t", "--terminal"):
			outputtoConsole(arg)
		else:
			sys.exit()

if __name__ == '__main__':
	main(sys.argv[1:])
	
