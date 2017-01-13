import text, memory, re

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
	trules = text._retext()
	elements=[]
	emoticons = list(re.finditer(_dict["emoticons"], review))
	if emoticons: elements.extend([e.group() for e in emoticons])
	if re.search(_dict["negation"], review):
		recontruct = ''; last=0
		for e in re.finditer(_dict["plckng"], review): 
			elements.extend(['!'+w for w in text.tokenize(e.group(), trules)])
			recontruct += review[last:e.start()]
			last = e.end()
		review = recontruct + review[last:]
	elements.extend(text.tokenize(review, trules))
	elements = filter(db.__contains__, elements)
	if elements:
		val = 0; size = 0		
		comp.extend([db[e] for e in elements])
		val += sum(comp); size += len(comp)
		return val / size
	return 0
