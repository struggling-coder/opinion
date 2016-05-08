'''Features under development
   BTW A lesson learnt. Do all data processing in SQL'''
import time
import rev
import dbctrl as d
import os

def normalization():
	'''Normalization using my database'''
	print "dafuq"
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	c = conn.cursor()
	print "connected"
	files = os.listdir("/home/aditya/Desktop/project/aclImdb/test/pos/")
	i=0
	l = d.handledb('adj')
	for file in files:
		i+=1
		if (i%50 ==0): 
			print str(i)+" files done"
			conn.commit()
		persc = rev.basic_scan(open("/home/aditya/Desktop/project/aclImdb/test/pos/"+file).read(), l, False)
		c.execute("update normalize set num = num + 1, persc = persc + "+str(persc)+" where score = "+((file.split(".")[0]).split("_")[1]))
		print persc 
		print ((file.split(".")[0]).split("_")[1])
		print "----"
	print "done."

def snapshot(name):
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	

def negation(review, adj=None):
	'''One deviation out'''		

def cmem(old, new):
	'''Competetive memory. Old vs new, then weight correct wrong to finally committing adj
	   Take snapshot first'''
	snapshot('adj')

def tlfow(review, adj=None):
	'''The lowest form of wit. It'll be awesome if I manage to teach this'''

def negation(review, adj=None):
	'''One deviation out'''

'''Tables in mem'''
#create table mem.normalize(score int, num int, persc float)
#create table mem.snap_adj(word varchar(20), pull float, times bigint)
#create table mem.adj(word varchar(20), pull float, times bigint)
#create table mem.rul_iftt(if varchar(25), then float)
#create table mem.rul_neg(if varchar(25), then float)