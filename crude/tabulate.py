'''
As the name of the folder says, this is the crude section for the solution that I am looking for. Maybe I can improve on this
'''

import text
import MySQLdb
import os

def tabulate(review, rating):
	tokens = (text.tokenize(review))
	c = db.cursor()
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
		c.execute("insert into words values('"+token+"', 1, "+ rating + ")")

def wrapper():
	#CREATE TABLE words(word, freq bigint, score bigint, av)
	db = MySQLdb.connect(passwd='aditya', db='crude')
	files = os.listdir("/home/aditya/Desktop/project/aclImdb/test/pos/")
	for file in files:
		tabulate(open("/home/aditya/Desktop/project/aclImdb/test/pos/"+file).read(), int((file.split(".")[0]).split("_")[1]))
	print len(files)+" files processed."
