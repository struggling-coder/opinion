import dbctrl, os, sys

def sntstruct(text, mode):
	'''Sentence structure applications'''
	if mode is 0:
		'''How many'''				
		return text.count('.') + text.count('?') + text.count('!') + text.count(',')



def wrdsinctxt(word, text):
	'''Returns the words in context to the particular word supplied'''
	if word not in text: return []
	#First check if review has more that one sentence
	#if sntstruct(text, 0) > 0:
	
	index = text.find(word)
	terminate = text[index:].find('.') 
	if terminate is -1: terminate = text[index:].find(',')
	if terminate is -1: terminate = text[index:].find('?')
	if terminate is -1: terminate = text[index:].find('!')
	#if terminate is -1: #Just one sentence or maybe the last sentence
	init = text[:index].find('.') 
	if init is -1: init = text[:index].find(',')
	if init is -1: init = text[:index].find('?')
	if init is -1: init = text[:index].find('!')
	
	if init is -1 and terminate is -1:
		return text
	else if init is -1: return text[:terminate]
	else if terminate is -1: return text[init:]
	else:
		return text[init:terminate]

def IFTTT(table):
	'''The start of basic AI deductions
	IFTTT
	create table replthis(if varchar(100), type varchar(100), then varchar(100))'''
	dbctrl.handledb(table)
	_dict={}

