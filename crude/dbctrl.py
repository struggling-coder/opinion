'''Python wrapper for database interaction'''
import time

def handledb(name, debug=False):
	if debug: handledb_debug(name)
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	if name is 'adj':
		cur = conn.cursor()
		cur.execute("select * from adj")
		_dict = {}
		for e in cur.fetchall():
			_dict[e[0]] = e[1]
		return _dict
	conn.close()

def snapshot(name):
	import MySQLdb as dbc
	_name = name+str(time.time())
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	c = conn.cursor()

	c.execute("use mem")
	c.execute("create table `"+_name+ "` like "+ name)
	conn.commit()
	c.execute("insert into `"+_name+ "` select * from "+name)
	conn.commit()
	return _name
	conn.close()

def handledb_debug(name):
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	print 'handledb: connection established to mem'
	if name is 'adj':
		cur = conn.cursor()
		cur.execute("select * from adj")
		_dict = {}
		for e in cur.fetchall():
			_dict[e[0]] = e[1]
		print 'handledb: returned '+str(len(_dict)) + ' entries'
		return _dict
	conn.close()
	print 'handledb: closed connection'	