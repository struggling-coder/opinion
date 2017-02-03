import text, memory, re, debug
#search for emoticons: [:;=<()] (not worth it?)

def learn(data, scores, rules=None, verbose=False, bar=None):
	if verbose: return learnd(data, scores, bar=bar)
	trules = text._retext(); j=0
	if rules is None: rules = learning()
	table1 = memory.control(0)
	table2 = memory.control(0)
	conn = memory.gc_(); cur = conn.cursor()
	if bar is not None: data = bar(data)
	for record in data:
		elements = basic(record, rules, trules, False)
		for e in elements: cur.execute("insert into "+table1+" values(\""+e+"\", "+str(scores[j])+", 1)")
		j += 1
	cur.execute("insert into "+table2+" select element, sum(score)/sum(times), sum(times) from "+table1+" group by element")
	memory.integrate(table2, cur)
	memory.forget(table1)
	conn.commit(); conn.close()

def learnd(data, scores, rules=None, bar=None):
	trules = text._retext(); j=0
	if rules is None: rules = learning()
	table1 = memory.control(0)
	table2 = memory.control(0)
	print "learn: temp = "+table1
	print "learn: temp = "+table2
	conn = memory.gc_(); cur = conn.cursor()
	print "learn: memory ready"
	if bar is not None: data = bar(data)
	for record in data:
		elements = basic(record, rules, trules, False)
		for e in elements: cur.execute("insert into "+table1+" values(\""+e+"\", "+str(scores[j])+", 1)")
		j += 1
	cur.execute("insert into "+table2+" select element, sum(score)/sum(times), sum(times) from "+table1+" group by element")
	print "learn: integrating tables"
	memory.integrate(table2, cur)
	print "learn: deleting temporary tables"
	memory.forget(table1)
	conn.commit(); conn.close()
	print "learn: committed to memory"

def basic(review, rules=None, trules=None, verbose=False):
	if rules is None: rules = learning()
	if trules is None: text._retext()
	if verbose: debug.basic(review, rules, trules)
	elements=[]; 
	#emoticons = list(re.finditer(rules[1], review))
	#if emoticons: elements.extend([e.group() for e in emoticons])
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
