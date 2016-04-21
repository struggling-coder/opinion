'''This is mostly the supervised part of supervised ML
'''
import dbctrl
import MySQLdb

def normalize():


def find_common_words():
	'''Read mem and find out the common words'''

	backup = dbctrl.snapshot()
	db = dbctrl.handledb('adj')
