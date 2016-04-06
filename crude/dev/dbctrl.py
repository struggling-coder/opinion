'''Python wrapper for database interaction'''

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