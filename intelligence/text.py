import re

def _retext():
	_dict={}
	_dict["clause"] = re.compile(r'[!?.,]')
	_dict["splitter"] = re.compile(r"([\w']{3,})") #TODO: check efficiency {3,} thing
	return _dict

def tokenize(textbody, regexp=None, debug=False):
	if regexp is None: regexp = _retext()
	_tokens = re.findall(regexp["splitter"], textbody)
	return [e.lower() for e in _tokens]

def tokenize_sentences(textbody, regexp=None, debug=False):
	if regexp is None: regexp = _retext()
	_tokens = re.split(regexp["clause"], textbody)
	for j in range(0, len(_tokens)):
		_tokens.insert(0 , re.findall(regexp["splitter"], _tokens.pop()))
	return (filter(bool, _tokens))
