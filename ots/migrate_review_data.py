'''	create database ref
	create table acm(num, )
'''

import os
import MySQLdb as dbc
conn = dbc.connect(user='root', passwd='aditya', db='ref')	

c = conn.cursor()

files = os.listdir("/home/aditya/Desktop/project/aclImdb/test/pos/")
i=0
for file in files:
	i+=1
	if (i%250 ==0): 
		print str(i)+" files done"
		db.commit()
	rev = open("/home/aditya/Desktop/project/aclImdb/test/pos/"+file).read()
	score = int((file.split(".")[0]).split("_")[1])
	c.execute("insert into revdata(review, score) values(\""+rev+"\", "+str(score)+")")

files = os.listdir("/home/aditya/Desktop/project/aclImdb/test/neg/")
i=0
for file in files:
	i+=1
	if (i%250 ==0): 
		print str(i)+" files done"
		db.commit()
	rev = open("/home/aditya/Desktop/project/aclImdb/test/neg/"+file).read()
	score = int((file.split(".")[0]).split("_")[1])
	c.execute("insert into revdata(review, score) values(\""+rev+"\", "+str(score)+")")
	