#!/usr/bin/python
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import codecs

from nltk import sent_tokenize

f = open("7pmid-sen-dnorm.txt",'r')
abstracts = f.read().strip().split("\n")

output=sys.stdout
outputfile=open('8pmid-abst-dnorm-cnv.txt','w')
sys.stdout=outputfile
for abstract in abstracts:
	values = abstract.strip().split("\t")

	#print len(values)
#for (num,values) in enumerate(f):
	if len(values)>=3: 
		text =str(values[3])
		#text=str(values[4:int(n)+4])
    		pmid = values[0]
    		#text = values[4] 

        	#print pmid
        	findallObja = re.findall( '(([1-9]\d?|[xyXY])[pqPQ][1-9]\d?([\-\~]?[pqPQ]?[1-9]\d?){0,}(\.[1-9]\d{0,1})*)', text ,re.I|re.L|re.M|re.S|re.U|re.X)
        	findallObjb = re.findall( r'([tT]risomy\s?([1-9][0-9]?|x)*)', text)
        	findallObjc = re.findall( r'\s[xX][xX][xX]\s', text)
        	findallObjd = re.findall( r'\s[xX][xX][yY]\s', text)
                if findallObja:
            		start=0
            		for a in range(len(findallObja)):
                		obja = findallObja[a]
                		index = text.find(obja[0],start)
                		outputfile.write(str(values)+str(index)+"-"+str(index+len(obja[0]))+"###"+obja[0]+"###"+obja[0]+"###"+str(index)+"-"+str(index+len(obja[0]))+"\n")
                		start = index+1
        	if findallObjb:
            		start=0
            		for b in range(len(findallObjb)):
                		objb = findallObjb[b]
                		index = text.find(objb[0],start)
                		outputfile.write(str(values)+str(index)+"-"+str(index+len(objb[0]))+"###"+objb[0]+"###"+objb[0]+"###"+str(index)+"-"+str(index+len(objb[0]))+"\n")
                		start = index+1
        	if findallObjc:
            		start=0
            		for c in range(len(findallObjc)):
                		objc = findallObjc[c]
                		index = text.find(objc[0],start)
                		outputfile.write(str(values)+str(index)+"-"+str(index+len(objc))+"###"+objc+"###"+objc+"###"+str(index)+"-"+str(index+len(objc))+"\n")
                		start = index+1
        	if findallObjd:
            		start=0
            		for d in range(len(findallObjd)):
                		objd = findallObjd[d]
                		index = text.find(objd[0],start)
                		outputfile.write(str(values)+str(index)+"-"+str(index+len(objd))+"###"+objd+"###"+objd+"###"+str(index)+"-"+str(index+len(objd))+"\n")
                		start = index+1
 	#else:
        
		#print(str(values[0])+ "\n") 
f.close()
outputfile.close()
sys.stdout=output

