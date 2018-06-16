#coding:utf-8  
import shutil  
readDir = "2output-sent.txt"  
writeDir = "3pmid-sen-a.txt"  
#txtDir = "/home/fuxueping/Desktop/１"  
lines_seen = set()  
outfile=open(writeDir,"w")  
f = open(readDir,"r")  
for line in f:  
    if line not in lines_seen:  
        outfile.write(line)  
        lines_seen.add(line)  
outfile.close()  
