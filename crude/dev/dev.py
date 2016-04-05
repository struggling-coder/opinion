'''Features under development'''
import time

def handledb(name):
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	if name is 'adj':
		cur = conn.cursor()
		cur.execute("select * from adj")
		_dict = {}
		for e in cur.fetchall():
			_dict[e[0]] = e[1]

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
#create table mem.snap_adj(word varchar(20), pull float, times bigint)
#create table mem.adj(word varchar(20), pull float, times bigint)
#create table mem.rul_iftt(if varchar(25), then float)
#create table mem.rul_neg(if varchar(25), then float)