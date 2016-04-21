'''This is mostly the supervised part of supervised ML
'''
import dbctrl
import MySQLdb
import rev

#create table negscan(path, given_score, my_score, deviation)
def negation():
	'''Current strategy is to operate on the set of reviews, and find out which don't match worst'''
	import MySQLdb as dbc
	conn = dbc.connect(user='root', passwd='aditya', db='mem')	
	dbctrl.snapshot('negscan')
	c= conn.cursor()

	c.execute("delete from negscan")
	conn.commit()

	i=0
	for file in files:
		i+=1
		if (i%250 ==0): 
			print str(i)+" files done"
			conn.commit()
		dude = open("/home/aditya/Desktop/project/aclImdb/test/pos/"+file).read()
		score = int((file.split(".")[0]).split("_")[1])
		_score = rev.basic_scan(dude)
		c.execute("insert into negscan values("+"'/pos/"+file+"', "+score+", "+_score+", "+abs(_score-score)+")")

	i=0
	for file in files:
		i+=1
		if (i%250 ==0): 
			print str(i)+" files done"
			conn.commit()
		dude = open("/home/aditya/Desktop/project/aclImdb/test/pos/"+file).read()
		score = int((file.split(".")[0]).split("_")[1])
		_score = rev.basic_scan(dude)
		c.execute("insert into negscan values("+"'/pos/"+file+"', "+score+", "+_score+", "+abs(_score-score)+")")



def normalize():
	'''Use a reference for all of the '10' reviews and all'''

def find_common_words():
	'''Read mem and find out the common words'''

	backup = dbctrl.snapshot()
	db = dbctrl.handledb('adj')
