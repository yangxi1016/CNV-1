#!/usr/bin/python
import psycopg2
import re
import sys
import codecs


def connect():
    conn = psycopg2.connect(database="pubmed", user="postgres", password="",
                            host="127.0.0.1", port="5432")
    return conn


def select(tb_name, condition):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("select * from {} where pmid =\'{}\'".format(tb_name, condition))
        rows = cur.fetchall()
        #print("select successfully")
        #print("select * from {} where pmid =\'{}\'".format(tb_name, condition))
        return rows
    except Exception as e:
        conn.rollback()  # 如果出错，则事务回滚
        #print(e)
    conn.close()


def get_cnv():
    output=sys.stdout
    outputfile=open('pmid-abst.txt','w')
    sys.stdout=outputfile
    with codecs.open("PMID.txt", "r", "utf-8") as f:
        for line in f.readlines():
            pmid = line.strip()
            
            rows = select("abstract",pmid)
            for r in rows:
                 outputfile.write(pmid+"\t"+r[2]+"\n")
                       
    f.close()
    outputfile.close()
    sys.stdout=output
   

if __name__ == "__main__":
    get_cnv()
