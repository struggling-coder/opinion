import text #outdated now
import dev
import dbctrl

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
	return pull/times
