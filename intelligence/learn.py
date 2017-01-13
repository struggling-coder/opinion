import text, memory, re
#search for emoticons: [:;=<()] (not worth it?)

def understand():
	'''
	1) Get the average filtered
	2)
	'''

def learn_v0(data, scores, rules=None, verbose=False):
	trules = text._retext(); j=0
	if rules is None: rules = learning()
	table1 = memory.control(0)
	conn = memory.gc_(); cur = conn.cursor()
	for record in data:
		elements = basic(record, rules, trules, False)
		for e in elements: cur.execute("insert into "+table1+" values("+e+", "+str(score[j])+")")
		j += 1
	table2 = memory.control(0)
	cur.execute("insert into "+table2+" select element, sum(score)/sum(times), sum(times) from "+table1+" group by element")
	memory.integrate(table2)

def basic(review, rules=None, trules=None, verbose=False):
	if rules is None: rules = learning()
	if trules is None: text._retext()
	elements=[]; 
	emoticons = list(re.finditer(rules[1], review))
	if emoticons: elements.extend([e.group() for e in emoticons])
	if re.search(rules[0], review):
		recontruct = ''; last=0
		for e in re.finditer(rules[2], review): 
			elements.extend(['!'+w for w in text.tokenize(e.group(), trules)])
			recontruct += review[last:e.start()]
			last = e.end()
		review = recontruct + review[last:]
	elements.extend(text.tokenize(review, trules))
	return elements

def learning():
	return [re.compile(r"\bNOT\b|\bBUT\b|\bNO\b|N'T\b", re.IGNORECASE),
	re.compile(r"([:;]|:'|X|B|=)-?[()\\\/\|p0Oo3DP\]\[]"),
	re.compile(r"(^|[.?!])*[\w\s'\",-]*?(\bno\b|\bbut\b|\bnot\b|n't\b)[\w\s'\",-]*?($|[.?!])", re.IGNORECASE)]
