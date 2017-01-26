import text, memory, re, progressbar, tools

def _re_analysis():
	_dict = {}
	_dict["negation"] = re.compile(r"\bNOT\b|\bBUT\b|\bNO\b|N'T\b", re.IGNORECASE)
	_dict["strong"] = re.compile(r'\bVERY\b', re.IGNORECASE)
	_dict["emoticons"] = re.compile(r"(([:;]|:'|X|B|=)-?[()\\\/\|p0Oo3DP\]\[])|<\/?3") 
	#can be improved
	_dict["plckng"] = re.compile(r"(^|[.?!])*[\w\s'\",-]*?(\bno\b|\bbut\b|\bnot\b|n't\b)[\w\s'\",-]*?($|[.?!])", re.IGNORECASE)
	_dict["noba"] = re.compile(r"[^.?!]*?\bnot\b[^.?!]*?\bbut\b[^.?!]*", re.IGNORECASE)
	return _dict
	
def analyze(review, db=None, regexp=None, debug=False):
	if regexp is None: regexp = _re_analysis()
	if db is None: db = memory.recollect()
	if debug: analyzed(review, db, regexp)
	trules = text._retext()
	elements=[]
	emoticons = list(re.finditer(regexp["emoticons"], review))
	if emoticons: elements.extend([e.group() for e in emoticons])
	if re.search(regexp["negation"], review):
		recontruct = ''; last=0
		for e in re.finditer(regexp["plckng"], review): 
			elements.extend(['!'+w for w in text.tokenize(e.group(), trules)])
			recontruct += review[last:e.start()]
			last = e.end()
		review = recontruct + review[last:]
	elements.extend(text.tokenize(review, trules))
	elements = filter(db.__contains__, elements)
	if elements:
		val = 0; size = 0		
		comp = ([db[e] for e in elements])
		val += sum(comp); size += len(comp)
		return val / size
	return 0

def analyzed(review, db, regexp):
	trules = text._retext()
	elements=[]
	emoticons = list(re.finditer(regexp["emoticons"], review))
	print "analyze: "+str(len(emoticons))+" emoticons found"
	if emoticons: elements.extend([e.group() for e in emoticons])
	if re.search(regexp["negation"], review):
		print "analyze: negation detected"
		recontruct = ''; last=0
		for e in re.finditer(regexp["plckng"], review): 
			elements.extend(['!'+w for w in text.tokenize(e.group(), trules)])
			recontruct += review[last:e.start()]
			last = e.end()
		print "analyze: "+str(len(elements)-len(emoticons))+" negatives found"
		review = recontruct + review[last:]
	elements.extend(text.tokenize(review, trules))
	elements = filter(db.__contains__, elements)
	print elements
	if elements:
		val = 0; size = 0		
		comp = ([db[e] for e in elements])
		val += sum(comp); size += len(comp)
		return val / size
	return 0

def _word(word):

	bar = progressbar.ProgressBar()
	data = tools.loaddir("/home/aditya/Desktop/project/aclImdb/train/pos/")
	data.extend(tools.loaddir("/home/aditya/Desktop/project/aclImdb/train/neg/"))
	print "analysis: "+"reading data and scores"
	scores=[0,0,0,0,0,0,0,0,0,0,0]
	for w in bar(data):
		list(re.finditer(word, open(w[0]).read(), re.IGNORECASE))
		scores[int(w[1])] += 1
	return scores