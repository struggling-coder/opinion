import text
import dbctrl, MySQLdb

datapath = ''

#create table normal_proc1(word varchar(20), freq int)
#create table normal_proc2(word varchar(20), times mediumint)

def assimilate_changes():
	'''Backup first. Make changes to cmem REMEMBER CMEM'''

def process_data(table_name):
	'''Think about it'''

def acquire_data(data, db=None, verbose=False):
	'''Use the data standard. This will require more work.'''

	if verbose: return acquire_data_verbose(data, db)

	if (db is None):
		db = dbctrl.handledb('adj')

	conn = MySQLdb.connect(user='root', passwd='aditya', db='mem')	
	c= conn.cursor()

	c.execute("delete from normal_proc1")
	c.execute("delete from normal_proc2")

	for e in data:
		whoosh = text.tokenize(e)
		for word in whoosh:
			c.execute("insert into normal_proc1 values('"+word+"', 1)")
		conn.commit()

	c.execute("insert into normal_proc2 select word, sum(freq) from normal_proc1 group by word")
	conn.commit()
	conn.close()

def acquire_data_verbose(data, db=None):
	
	if (db is None):
		db = dbctrl.handledb('adj')

	conn = MySQLdb.connect(user='root', passwd='aditya', db='mem')	
	c= conn.cursor()

	print "connection openend to mem"

	c.execute("delete from normal_proc1")
	c.execute("delete from normal_proc2")

	print 'data wiped'

	for e in data:
		whoosh = text.tokenize(e)
		print 'text tokenized'
		for word in whoosh:
			c.execute("insert into normal_proc1 values('"+word+"', 1)")
		conn.commit()

	print 'table 1 done'

	c.execute("insert into normal_proc2 select word, sum(freq) from normal_proc1 group by word")
	conn.commit()

	print 'table 2 done'
	conn.close()

def get_data_linux():
	'''Whatever'''