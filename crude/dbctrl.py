'''Python wrapper for database interaction'''
import time

def pickle_adj(pickle):
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	cur = conn.cursor()
	cur.execute("delete from adj")
	for e in pickle:
		cur.execute("insert into adj values('"+e+"',"+pickle[e]+" )")
	conn.commit()
	conn.close()

def inetc(database, name, query):
	'''If Not Exists Then Create'''
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db=database)	
	cur = conn.cursor()
	cur.execute("show tables")
	dat = cur.fetchall()
	for i in dat:
		if i[0] == name:
			return None
	cur.execute(query)
	conn.commit()
	conn.close()	

def handledb(name, debug=False):
	if debug: return handledb_debug(name)
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

def snapshot(name, database='mem'):
	import MySQLdb as dbc
	_name = name+str(time.time())
	conn = dbc.connect(user='root', passwd='aditya', db=database)	
	c = conn.cursor()

	c.execute("use mem")
	c.execute("create table `"+_name+ "` like "+ name)
	conn.commit()
	c.execute("insert into `"+_name+ "` select * from "+name)
	conn.commit()
	return _name
	conn.close()

def restore(name):
	'''Restore from most recent snapshot'''
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	c = conn.cursor()
	c.execute("show tables like '"+name+"%'")
	w = c.fetchall()
	backup = w[len(w) - 1][0]
	c.execute("delete from `"+name+"`")
	c.execute("insert into "+name+" select * from `"+backup+"`")
	conn.commit()
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