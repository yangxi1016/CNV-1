#!/usr/bin/python  
#coding = UFT-8
import os,sys
import re


output=sys.stdout
outputfile=open('9pkde4j-format.txt','w')
sys.stdout=outputfile
f = open( r"8pmid-abst-dnorm-cnv.txt" , "r" )  


lines = f.readlines()

for line in lines:
        
	line = line.replace("', '","	")
	line = line.replace("['","")
	line = line.replace("']","")
        line = line.replace("',  "," ")
	
        line = line.replace("', ","	")
	line = line.replace(' ", "'," 	")
        line = line.replace(", '"," 	")
        line = line.replace("'  '"," ")

	line = line.replace("', ","")

        line = line.replace("'","")

	line = line.replace('"',"") 
        
        line = line.replace(' ",'," 	")
	line = line.replace("]","")
        line = line.replace("% ","%")
	line = line.replace("%']","%")
 	line = line.replace("'#","#")
	
	
	
	print line,

outputfile.close()
sys.stdout=output
