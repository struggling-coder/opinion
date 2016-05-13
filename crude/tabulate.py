'''
As the name of the folder says, this is the crude section for the solution that I am looking for. Maybe I can improve on this
'''

import text
import MySQLdb
import os

def tabulate(review, rating, z):
	tokens = set(text.tokenize(review))
	c = z.cursor()
	#c.execute("SELECT word FROM words")
	#_data = c.fetchall() #Poorly constructed connector (not really)
	#data=[]
	#for e in _data:
	#	data.append(e[0])
	#_int = tokens.intersection(set(data))
	'''for token in _int:
		c.execute("update words set freq = freq + 1 and score = score + " + str(rating))
		tokens.remove(token)'''
	for leftovers in tokens:
		c.execute("insert into words values('"+leftovers+"', 1, "+ str(rating) + ", 0)")

def wrapper():
	#CREATE TABLE words(word, freq bigint, score bigint, av)
	db = MySQLdb.connect(user='root', passwd='aditya', db='mem')
	print "connection opened to mem"
	files = os.listdir("/home/aditya/Desktop/project/aclImdb/train/neg/")
	i=0
	for file in files:
		i+=1
		if (i%250 ==0): 
			print str(i)+" files done"
			db.commit()
		tabulate(open("/home/aditya/Desktop/project/aclImdb/train/neg/"+file).read(), int((file.split(".")[0]).split("_")[1]), db)
	cur = db.cursor()
	print str(len(files))+" files processed."
	cur.execute("update words set av = score/freq")
	db.close()
	print "averages updated"

def group():
	db = MySQLdb.connect(user='root', passwd='aditya', db='mem')
	print "connection opened to mem"
	cur = db.cursor()
	print cur.execute("select word from words")
	_data = cur.fetchall() #Poorly constructed connector (not really)
	data=[]
	for e in _data:
		data.append(e[0])
	data = list(set(data))
	print str(len(data)) + ' unique keys generated'
	i=0
	for word in data:
		i+=1; 
		if (i%250 ==0): 
			print str(i)+" words done"
		db.commit()
		cur.execute("select * from words where word = '"+word+"'")
		_data = cur.fetchall() #Poorly constructed connector (not really)
		tsum=0
		tval=0.0
		for en in _data:
			tsum +=1; tval += en[2]
		cur.execute("insert into crav values('"+ word+"',  "+str(tval/tsum) +", "+str(tsum)+")")
		

##############################################################################################################

#create table amznfd(id bigint, productid varchar(10), hn int, hd int, score int, sum varchar(100), rev varchar(750))
def insert_amazon_data():
	'''From kaggle.com: Amazon Fine Foods Review. Useful for testing'''
	i=0
	db = MySQLdb.connect(user='root', passwd='aditya', db='crude')
	fil = open("/home/aditya/Desktop/project/AmazonFoodReview.csv", "r")
	print "connection opened to crude"
	cur = db.cursor()
	for line in fil.read().split(',,,,,,,,,,,,,,,,,,,'):
		i+=1
		if (i%1000) == 0: print str(i) +" records committed"
		data = line.split(",")
		cur.execute("insert into amznfd values("+data[0]+", '"+data[1]+"',"+data[4]+","+data[5]+","+data[6]+" ,'"+data[8]+"','"+data[9]+"')")
		db.commit()
