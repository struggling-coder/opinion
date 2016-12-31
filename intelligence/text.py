import re

def _retext():
	_dict={}
	#_dict["negation"] = re.compile(r'\bNOT\b|\bBUT\b|\bNO\b', re.IGNORECASE)
	#_dict["strong"] = re.compile(r'\bVERY\b', re.IGNORECASE)
	#_dict["emoticons"] = re.compile(r"(([:;]|:'|X|B|=)-?[()\\\/\|p0Oo3DP\]\[])|<\/?3")
	#_dict["alphabet"] = re.compile(r'[A-Za-z]')
	_dict["clause"] = re.compile(r'[!?.,]')
	_dict["splitter"] = re.compile(r"([\w']+)")
	return _dict

def tokenize(textbody, regexp=None, debug=False):
	if regexp is None: regexp = _retext()
	_tokens = re.split(regexp["clause"], textbody)
	for j in range(0, len(_tokens)):
		_tokens.insert(0 , re.findall(regexp["splitter"], _tokens.pop()))
	return (filter(bool, _tokens))
