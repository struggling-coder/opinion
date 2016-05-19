'''Functions realating to bodies of text'''

soa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pml = ['!','?']
symbols = ['!','?']
punctuation = ['!','?','.',',',';',':','+','-','@','#','%','&','*','(',')']
emoticons = ['O.O','O.o','o.O','o.o',
			 '\\m/',
			 ':)',':(',':|',':\\',':/',':*',':@',':O',':]',':[',
			 ':-)',':-(',':-|',':-\\',':-/',':-*',':-@',':-O',':-]',':-[',
			 ':D',':p',':d',':P',
			 ':-D',':-p',':-d',':-P',
			 ';-D',';-p',';-d',';-P',
			 ';D',';p',';d',';P',
			 ';-)',';-(',';-|',';-\\',';-/',';-*',';-@',';-O',';-]',';-[',
			 ';)',';(',';|',';\\',';/',';*',';@',';O',';]',';[',
			 '::',
			 '=)','=(','=|','=\\','=/','=*','=@','=O','=]','=[',
			 '=-)','=-(','=-|','=-\\','=-/','=-*','=-@','=-O','=-]','=-[',
			 '=D','=p','=d','=P',
			 '=-D','=-p','=-d','=-P'
			 ]
emo_id=set([':',';','O.','o.','='])
emoticons_positive=[
':D',':p',':P',
':-D',':-p',':-P',
':)',':*',':]',
':-)',':-*',':-]',
':O',':-O',
';)',';*',';]'
';-)',';-*',';-]'
'=)','=D','=]'
]
emoticons_negative=[
':(',':[',
';(',';[',
'=(',
':\\',':/',':|'
]
common = [
]
helping_verbs = ['am', 'are', 'is', 'was', 'were', 'being', 'been', 'have', 'has', 'had',
				 'shall', 'will', 'do', 'does', 'did', 'may', 'might', 'can', 'could', 'would', 'should']

negatives = ['not', 'but','no']

def dev_tokenize(text):
	print 'hello'

#this can be pruned
def tokenize(text):
	'''Return tokens from formatted text'''
	text=text.strip().lower()
	text.replace('.',' ').replace('?',' ').replace('!',' ').replace(',',' ').replace('\n',' ')
	words=[]
	for word in text.split(' '):
		if len(set(word).intersection(set(soa))) > 0:
			if word[len(word)-1].isalpha() is False:
				while word[len(word)-1].isalpha() is False:
					word = word.rstrip(word[len(word)-1])
			elif word[0].isalpha() is False:
				while word[0].isalpha() is False:
					word = word.lstrip(word[0])
			word = word.strip()
			if word.isalpha() is False:
				for letter in word:
					if letter.isalpha() is False and letter is not ' ':
						try:
							subwords = word.split(letter)
							word = subwords[1]
							words.append(subwords[0])
						except IndexError:
							word =''
				if ' ' in word:
					subw = word.split(' ')
					for sw in subw:
						if sw is '':
							subw.remove(sw)
					if len(subw) >= 2:
						word = subw[0]
						subw.remove(word)
						for temp in subw:
							words.append(temp)
					elif len(subw) == 1:
						word = subw[0]
					else:
						word = ''
			if word is not '':
				words.append(word)
		for entry in words:
			if entry == '':
				words.remove(entry)
	return words

def split_sentences(text):
	'''Seperate the sentences into an array'''
	array=[]
	for phrase in text.split('.'):
		if len(set(symbols).intersection(set(phrase))) > 0:
			set_ = phrase.split('!')
			if len(set_) > 1:
				phrase = set_[0]
				array.append(set_[1].strip().lower())
			else:
				set_ = phrase.split('?')
				phrase = set_[0]
				array.append(set_[1].strip().lower())
		array.append(phrase.strip().lower())
	for entry in array:
		if entry is '':
			array.remove(entry)
	return array

def split_sentence(sentence):
	'''Split a sentence into words'''
	text=sentence
	array=[]
	text=text.strip().lower()
	text.replace('.',' ').replace(',',' ').replace('\n',' ')
	words=[]
	for word in text.split(' '):
		if len(set(word).intersection(set(soa))) > 0:
			if word[len(word)-1].isalpha() is False:
				while word[len(word)-1].isalpha() is False:
					word = word.rstrip(word[len(word)-1])
			elif word[0].isalpha() is False:
				while word[0].isalpha() is False:
					word = word.lstrip(word[0])
			word = word.strip()
			if word.isalpha() is False:
				for letter in word:
					if letter.isalpha() is False and letter is not ' ':
						try:
							subwords = word.split(letter)
							word = subwords[1]
							words.append(subwords[0])
						except IndexError:
							word =''
				if ' ' in word:
					subw = word.split(' ')
					for sw in subw:
						if sw is '':
							subw.remove(sw)
					if len(subw) >= 2:
						word = subw[0]
						subw.remove(word)
						for temp in subw:
							words.append(temp)
					elif len(subw) == 1:
						word = subw[0]
					else:
						word = ''
			if word is not '':
				words.append(word)
		for entry in words:
			if entry == '':
				words.remove(entry)
	return words

def get_word_count(text):
	'''Returns the word count of a text'''
	text = text.strip().lower()
	text.replace('.',' ').replace('?',' ').replace('!',' ').replace(',',' ').replace('\n',' ')
	return len(text.split(' '))

def get_database_intersections(text):
	'''Returns the common records shared with the database'''
	import sentimentdb 
	records=sentimentdb.read().keys()
	tokens=tokenize(text)
	return list(set(records).intersection(set(tokens)))

def get_number_intersections(text):
	'''Returns the number of common records with the database'''
	import sentimentdb 
	records=sentimentdb.read().keys()
	tokens=tokenize(text)
	return len(set(records).intersection(set(tokens)))

def has_database_intersections(text):
	'''Whether a text has SSR references'''
	if get_number_intersections(text) > 0:
		return True
	return False

def depuctuate(text):
	'''Remove any punctuation in a sentence'''
	
	matter=text
	for symbol in punctuation:
		matter.replace(symbol,' ')
	return matter

def has_emoji(text):
	'''Does the sentence contain emoticons?'''
	
	if len(set(text).intersection(emo_id))>0: return True
	return False

def extract_emoji(text):
	'''Remove emoticons from a sentence'''
	print '[text]: TODO extrace EMOJI'
	#TODO
	return

def convert_date_twitter(date):
	'''Return the proper converted date'''
	#Sat, 04 May 2013 21:31:32
	from datetime import datetime
	months={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
	date = date.strip().lstrip(date[0:5])
	array = date.split()
	time = array[len(array)-1]
	minute = int(time.split(':')[1])
	second = int(time.split(':')[2])
	hour   = int(time.split(':')[0])
	date   = int(array[0])
	month  = int(months[array[1]])
	year   = int(array[2])
	return datetime(year, month, date, hour, minute, second)

def truncate(value, places):
	value = str(value)
	return value[0:places]

def get_adj_density(sentence):
	'''Get the density of the adjectives present in a sentence'''

	import math
	adjectives=get_database_intersections(sentence)

	def wordlevel(sentence):
		adjectives_c=float(len(adjectives))
		words=float(len(tokenize(sentence)))
		return (adjectives_c/words) * 100

	def charlevel(sentence):
		letters=len(list(sentence))
		letters_a=0.0
		for adj in adjectives:
			letters_a+=len(list(adj))
		return ((math.sqrt(letters_a**3))/letters) * 100

	p1=wordlevel(sentence)
	p2=charlevel(sentence)

	return ((60.0/100) * p1) + ((40.0/100) * p2)

	

def get_length(text):
	'''
	Get the length of a supplied text
	'''
	if ' ' not in text.strip(): return 'word'
	elif '.' not in text.strip(): return 'sentence'
	else: return 'review'