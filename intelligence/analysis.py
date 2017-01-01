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
	data = text.tokenize(review)
	adjectives = filter(db.__contains__, data)
	if adjectives:
		val = 0; size = 0
		if re.search(regexp["negation"], review):
			for e in re.findall(regexp["plckng"], review)
				if 
		comp = [db[e] for e in re.findall(regexp["emoticons"], review)]
		comp.extend([db[e] for e in adjectives])
		val += sum(comp); size += len(comp)
		return val / size
