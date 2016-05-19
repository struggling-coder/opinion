import learn, os

def find_good_in_bad():
	#a simple grep should do it.

def learn_v1():
	'''Select 50 positive and 50 negative reviews from train. Make 2 lists and supply them. Capture output and then code same 
	structure into MySQL. Backup first'''

	data = []
	expec = []

	files = os.listdir("/home/aditya/Desktop/project/aclImdb/train/neg/")
	for file in files[0:50]:
		data.append(open("/home/aditya/Desktop/project/aclImdb/train/neg/"+file).read())
		expec.append(int((file.split(".")[0]).split("_")[1]))
	files = os.listdir("/home/aditya/Desktop/project/aclImdb/train/pos/")
	for file in files[0:50]:
		data.append(open("/home/aditya/Desktop/project/aclImdb/train/pos/"+file).read())
		expec.append(int((file.split(".")[0]).split("_")[1]))

	print "data collected.\nsending to learn.do"
	r = learn.do(data, expec)

	import MySQLdb 
	dbw = MySQLdb.connect(user='root', passwd='aditya', db='mem')
	print "connection opened to mem"
	cur = dbw.cursor()
	
	j=0
	for e in r:
		cur.execute("insert into memtest values('"+e+"', "+str(r[e])+")")
		if (j%250 == 0):
			dbw.commit()
		j+=1
	dbw.close()
