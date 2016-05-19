'''The point of this project
First stop: Mr. Bayes, the Naive'''

import dbctrl
import text
import os
import calibration
import normal
from text import negatives

#create table adj(word varchar(20), pull float)

#_dict[word] = []
def do(data, expec):
	'''Naive work indeed'''

	_dict = {}
	_return = {}
	i=0
	numbers = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	for e in expec:
		numbers[e] += 1
	p_rev_eq_k = [0,0,0,0,0,0,0,0,0,0,0]
	num = len(expec)
	for i in range(1,11):
		p_rev_eq_k[i] = numbers[i]/num
	print "data initialized"

	#while learning it doesn't really matter how many times this appears. OR DOES IT?
	i=0
	for e in data:
		buildup=[]
		for s in text.split_sentences(e):
			words=text.tokenize(s)
			builder=[]
			if len(set(words).intersection(set(negatives))) > 0:
				for d in words:
					builder.append("!"+d)
			else:
				builder.extend(words)
			buildup.extend(builder)
		for w in (buildup):
			try:
				_dict[w][expec[i]] +=1
			except KeyError:
				_dict[w] = [0,0,0,0,0,0,0,0,0,0,0]
				_dict[w][expec[i]] +=1
		i+=1
	print "data loaded. " + str(len(_dict)) + " words present"

	print 'commence pruning'
	q=0
	av=0
	for w in _dict.keys():
		av += sum(_dict[w])
	av = av / len(_dict)
	av *= 0.9 
	print str(av) + " is the threshold"
	for w in _dict.keys():
		if sum(_dict[w]) < av:
			_dict.pop(w)
			q+=1
	print str(q) + ' records removed'
	
	i=0
	for w in _dict.keys():
		score = 0
		p_word_in_rev = 0
		for j in range(1,11):
			try: p_word_in_rev += (_dict[w][j]/numbers[j])*p_rev_eq_k[j]
			except: p_word_in_rev += 0
		weights = [0,0,0,0,0,0,0,0,0,0,0]
		for j in range(1,11):
			try: weights[j] = (_dict[w][j]/numbers[j])*p_rev_eq_k[j]/p_word_in_rev
			except: weights[j] = 0
		for j in range(1,11):
			score += weights[j] * j
		_return[w] = [score,sum(_dict[w])]
	print 'data processed'

	print 'task complete'

	return _return

def implementation1():
	data = []
	expec = []

	b=0
	files = os.listdir("/home/aditya/Desktop/project/aclImdb/train/neg/")
	for file in files[:]:
		if (b%2500==0): print str(b)+ " negative files done"
		data.append(open("/home/aditya/Desktop/project/aclImdb/train/neg/"+file).read())
		expec.append(int((file.split(".")[0]).split("_")[1]))
		b+=1
	files = os.listdir("/home/aditya/Desktop/project/aclImdb/train/pos/")
	b=0
	for file in files[:]:
		if (b%2500==0): print str(b)+ " positive files done"
		data.append(open("/home/aditya/Desktop/project/aclImdb/train/pos/"+file).read())
		expec.append(int((file.split(".")[0]).split("_")[1]))
		b+=1
	print "data collected.\nsending to learn.do"
	r = do(data, expec)

	import MySQLdb 
	dbw = MySQLdb.connect(user='root', passwd='aditya', db='mem')
	print "connection opened to mem"
	cur = dbw.cursor()
	dbctrl.snapshot('adj')

	j=0
	for e in r:
		cur.execute("insert into adj values('"+e+"', "+str(r[e][0])+", "+str(r[e][1])+")")
		if (j%2000 == 0):
			dbw.commit()
			print str(j) + " words committed"
		j+=1
	dbw.close()

def dont_do(data, expec):
	''''''
	learnt = {}
	i = 0

	for e in data:
		words = text.tokenize(e)
		for w in words:
			if w not in learnt.keys(): 
				learnt[w] = [expec[i], 1]
			else:
				learnt[w][0] += expec[i]
				learnt[w][1] += 1
		i+=1

	#finally, remember this
	dbctrl.snapshot('adj')
	dbctrl.pickle_adj(learnt)