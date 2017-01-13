#Stupidest part of the whole thing
import MySQLdb, random
db='memory0'

#def origin():

def integrate(table):
	backup()
	conn = gc_(); cur = conn.cursor()
	cur.execute("delete from mem")
	cur.execute("insert into mem select * from "+table)
	forget(table)
	conn.close()

def control(_int):
	conn = gc_(); cur = conn.cursor()
	if _int is 0: #create table _tempXXXX(element varchar(15), score float, times int)
		name = '_temp'+str(random.randint(1000, 9999))
		cur.execute("create table "+name+"(element varchar(15), score float, times int)")
	if _int is 1:
		name = '_mem'+str(random.randint(1000, 9999))
		cur.execute("create table "+name+" like mem")
	conn.close()
	return name

def gc_():		
	return dbc.connect(user='root', passwd='aditya', db=db)	

def recollect():
	conn = gc_(); cur = conn.cursor()
	cur.execute("select * from mem"); conn.close()
	return {e[0]: e[1] for e in cur.fetchall()}

def backup():
	conn = gc_(); cur = conn.cursor()
	cur.execute("insert into "+control(1)+" select * from mem")

def forget(name):
	gc_().cursor().execute("drop table "+name)

def death():
	gc_().cursor().execute("drop database "+db)
"""
Master tables:
1) mem(element varchar(15), score float)
2) _mem**** [previous iterations of mem]

"""	