#!/usr/bin/python  
#coding = UFT-8
import os,sys
import re
result=[]
output=sys.stdout
outputfile=open('5pmid-sen-dnorm.txt','w')
sys.stdout=outputfile
f = open( r"3pmid-sen-a.txt" , "r" )  
a = open( r"4pmid-dnorm.txt", "r" )   
lines = f.readlines()
lists = []
lines_a = a.readlines()
lists_a = []
for line in lines:
        lists.append(line.split())
        
for line_a in lines_a:
        lists_a.append(line_a.split())
#print len(lists),len(lists_a)
for i in range(0,len(lists)-1):
	for j in range(0,len(lists_a)-1):

	
			#outputfile.write (str(len(lists))+"\n")
			#outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"\n")
                if (len(lists[i])>=5)&(len(lists_a[j])>=4)&(int(lists[i][0])==int(lists_a[j][0])):
			n =int(lists[i][3])
			x=str(lists[i][4:int(n)+4])
			if (int(lists[i][2])<=int(lists_a[j][1]))&(int(lists[i][3])>=int(lists_a[j][2])):
	
				outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+str(x)+"\t"+str(int(lists_a[j][1])-int(lists[i][2]))+"-"+str(int(lists_a[j][2])-int(lists[i][2]))+"###"+lists_a[j][3]+"###"+lists_a[j][3]+"###"+str(int(lists_a[j][1])-int(lists[i][2]))+"-"+str(int(lists_a[j][2])-int(lists[i][2]))+"%%%"+"\n")
			#outputfile.write(str(lists[i][0])+"\t"+lists[i][1]+"\t"+lists[i][2]+"-"+lists[i][3]+"\t"+"\t"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"###"+lists_a[j][3]+"###"+lists_a[j][3]+"###"+str(int(lists_a[j][1]))+"-"+str(int(lists_a[j][2]))+"%%%"+"\n")

		#else:
			#outputfile.write(str(lists[i])+"\n")
outputfile.close()
sys.stdout=output
