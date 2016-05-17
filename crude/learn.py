'''The point of this project
First stop: Mr. Bayes, the Naive'''

import dbctrl
import text

def do()

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
		i++

	#finally, remember this
	dbctrl.snapshot('adj')
	dbctrl.pickle_adj(learnt)