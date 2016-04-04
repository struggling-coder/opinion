'''
As the name of the folder says, this is the crude section for the solution that I am looking for. Maybe I can improve on this
'''

import text
import MySQLdb
import os

def tabulate(review, rating, z):
	tokens = set(text.tokenize(review))
	c = z.cursor()
	c.execute("SELECT word FROM words")
	_data = c.fetchall() #Poorly constructed connector (not really)
	data=[]
	for e in data:
		data.append(e[0])
	_int = tokens.intersection(set(data))
	for token in _int:
		c.execute("update words set freq = freq + 1 and score = score + " + rating)
		tokens.remove(token)
	for leftovers in tokens:
		c.execute("insert into words values('"+leftovers+"', 1, "+ str(rating) + ", 0)")

def wrapper():
	#CREATE TABLE words(word, freq bigint, score bigint, av)
	db = MySQLdb.connect(user='root', passwd='aditya', db='crude')
	print "connection opened to crude"
	files = os.listdir("/home/aditya/Desktop/project/aclImdb/test/neg/")
	for file in files:
		tabulate(open("/home/aditya/Desktop/project/aclImdb/test/neg/"+file).read(), int((file.split(".")[0]).split("_")[1]), db)
		db.commit()
	cur = db.cursor()
	print len(files)+" files processed."
	cur.execute("update words set av = score/freq")
	db.close()
	print "averages updated"

def group():
	db = MySQLdb.connect(user='root', passwd='aditya', db='crude')
	print "connection opened to crude"
	cur = db.cursor()
	print cur.execute("select word from words")
	_data = cur.fetchall() #Poorly constructed connector (not really)
	data=[]
	for e in _data:
		data.append(e[0])
	data = list(set(data))
	print str(len(data)) + 'unique keys generated'
	i=0
	for word in data:
		i+=1; 
		if (i%250 ==0): 
			print str(i)+" words done"
		cur.execute("select * from words where word = '"+word+"'")
		_data = cur.fetchall() #Poorly constructed connector (not really)
		tsum=0
		tval=0.0
		for en in _data:
			tsum +=1; tval += en[2]
		cur.execute("insert into crav values('"+ word+"',  "+str(tval/tsum) +", "+str(tsum)+")")
		#db.commit()
