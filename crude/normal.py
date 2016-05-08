import text
import dbctrl, MySQLdb

datapath = ''

def process_data(table_name):
	'''Think about it'''

#create table normal_proc1(word varchar(20))
#create table normal_proc2(word varchar(20), times mediumint)
def acquire_data(data, db=None):
	'''Use the data standard. This will require more work.'''

	if (db=None):
		db = dbctrl.handledb('adj')

	conn = MySQLdb.connect(user='root', passwd='aditya', db='mem')	
	c= conn.cursor()

	c.execute("delete from normal_proc1")
	c.execute("delete from normal_proc2")

	for e in data:
		whoosh = text.tokenize(e)
		for word in whoosh:
			c.execute("insert into normal_proc1 values('"+word+"')")
		conn.commit()

	c.execute("insert into normal_proc2 select word, sum(freq) from normal_proc1 group by word")
	conn.commit()
	conn.close()

def get_data_linux():
