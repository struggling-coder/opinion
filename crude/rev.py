import text #outdated now
import dbctrl
from text import negatives

def scan(review, db=None):
	if db is None:
		db = dbctrl.handledb('adj')
	buildup=[]
	for s in text.split_sentences(review):
		words=text.tokenize(s)
		builder=[]
		if len(set(words).intersection(set(negatives))) > 0:
			for d in words:
				builder.append("!"+d)
		else:
			builder.extend(words)
		buildup.extend(builder)

	times=0
	pull=0
	for word in set(words):
		c = words.count(word)
		if (c>0 and (word in db.keys())):
			pull += c * db[word]
			times += c
	if times is 0: return 0
	return pull/times
	
def better_scan(review, db=None):
	if db is None:
		db = dbctrl.handledb('adj')
	words = text.tokenize(review)
	
def basic_scan(review, db=None, debug=False):
	if debug:
		basic_scan_debug(review, db)
	'''The crudest form of matching'''
	if db is None:
		db = dbctrl.handledb('adj')
	words = text.tokenize(review)
	times=0
	pull=0
	for word in set(words):
		c = words.count(word)
		if (c>0 and (word in db.keys())):
			pull += c * db[word]
			times += c
	if times is 0: return 0
	return pull/times

def basic_scan_debug(review, db=None):
	if db is None:
		db = dbctrl.handledb('adj', True)
	words = text.tokenize(review)
	print 'basic_scan: '+str(len(words))+' words scanned'
	times=0
	pull=0
	print set(words)
	for word in set(words):
		c = words.count(word)
		if (c>0 and (word in db.keys())):
			pull += c * db[word]
			times += c
	if times is 0: return 0
	return pull/times
