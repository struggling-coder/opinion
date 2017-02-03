import re, text, analysis

#def human(text):

def basic(review, rules, trules):
	elements=[]; 
	emoticons = list(re.finditer(rules[1], review))
	print str(len(emoticons)) + " emoticons found"
	if emoticons: elements.extend([e.group() for e in emoticons])
	print elements
	if re.search(rules[0], review):
		print "negatives detected"
		recontruct = ''; last=0
		for e in re.finditer(rules[2], review):
			elements.extend(['!'+w for w in text.tokenize(e.group(), trules)])
			recontruct += review[last:e.start()]
			last = e.end()
		review = recontruct + review[last:]
	elements.extend(text.tokenize(review, trules))
	return elements

