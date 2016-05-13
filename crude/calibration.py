'''This is mostly the supervised part of supervised ML
'''
import dbctrl
import MySQLdb
import rev
import math
import os

#create table negscan(path, given_score, my_score, deviation)

def cmem():
	'''Compete in between the list of supplied tables for the best one. Add weightwise'''

def purge_common_words():
	'''WARNING: Run this only after an automated construct'''
	dbctrl.snapshot('adj')
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	c= conn.cursor()
	c.execute("delete from adj order by times desc limit 30")
	conn.commit(); conn.close()

def negation():
	'''Current strategy is to operate on the set of reviews, and find out which don't match worst'''
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	dbctrl.snapshot('negscan')
	c= conn.cursor()
	rec = 0; dev2 = 0

	c.execute("delete from negscan")
	conn.commit()

	files = os.listdir("/home/aditya/Desktop/project/aclImdb/test/pos/")
	i=0
	l = dbctrl.handledb('adj')
	for file in files:
		i+=1
		if (i%250 ==0): 
			print str(i)+" files done"
			conn.commit()
		dude = open("/home/aditya/Desktop/project/aclImdb/test/pos/"+file).read()
		score = int((file.split(".")[0]).split("_")[1])
		_score = rev.basic_scan(dude, l)
		c.execute("insert into negscan values("+"'/pos/"+file+"', "+str(score)+", "+str(_score)+", "+str(abs(_score-score))+")")
		rec += 1; dev2 += (_score-score)*(_score-score)

	files = os.listdir("/home/aditya/Desktop/project/aclImdb/test/neg/")
	i=0
	for file in files:
		i+=1
		if (i%250 ==0): 
			print str(i)+" files done"
			conn.commit()
		dude = open("/home/aditya/Desktop/project/aclImdb/test/neg/"+file).read()
		score = int((file.split(".")[0]).split("_")[1])
		_score = rev.basic_scan(dude, l)
		c.execute("insert into negscan values("+"'/neg/"+file+"', "+(score)+", "+(_score)+", "+(abs(_score-score))+")")
		rec += 1; dev2 += (_score-score)*(_score-score)

	stddev = math.sqrt(dev2/rec)
	flagged = []
	#TODO: COMPLETE THIS ######

def normalize():
	'''Use a reference for all of the '10' reviews and all'''


def find_common_words():
	'''Read mem and find out the common words'''

	backup = dbctrl.snapshot()
	db = dbctrl.handledb('adj')
