'''The point of this project
First stop: Mr. Bayes, the Naive'''

import dbctrl
import text

#create table adj(word varchar(20), pull float)

#_dict[word] = []
def do(data, expec):
	'''Naive work indeed'''

	_dict = {}
	_return = {}
	i=0
	numbers = [0,0,0,0,0,0,0,0,0,0,0]
	for e in expec:
		numbers[e] += 1
	p_rev_eq_k = [0,0,0,0,0,0,0,0,0,0,0]
	num = len(expec)
	for i in range(1,11):
		p_rev_eq_k[i] = numbers[i]/num
	print "data initialized"

	i=0
	for e in data:
		for w in text.tokenize(e):
			try:
				_dict[w][expec[i]] +=1
			except KeyError:
				_dict[w] = [0,0,0,0,0,0,0,0,0,0,0]
				_dict[w][expec[i]] +=1
		i+=1
	print "data loaded. " + str(len(_dict)) + " words present"

	i=0
	for w in _dict.keys():
		score = 0
		p_word_in_rev = 0
		for j in range(1,11):
			try: p_word_in_rev += (_dict[w][j]/numbers[j])*p_rev_eq_k[j]
			except: p_word_in_rev += 0
		weights = [0,0,0,0,0,0,0,0,0,0,0]
		for j in range(1,11):
			try: weights[j] = (_dict[w][j]/numbers[j])*p_rev_eq_k[j]
			except: weights[j] = 0
		for j in range(1,11):
			score += weights[j] * j
		_return[w] = score
	print 'data processed'

	print 'task complete'
	return _return

def dont_do(data, expec):
	''''''
	learnt = {}
	i = 0

	for e in data:
		words = text.tokenize(e)
		for w in words:
			if w not in learnt.keys(): 
				learnt[w] = [expec[i], 1]
			else:
				learnt[w][0] += expec[i]
				learnt[w][1] += 1
		i+=1

	#finally, remember this
	dbctrl.snapshot('adj')
	dbctrl.pickle_adj(learnt)