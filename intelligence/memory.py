#Stupidest part of the whole thing
import MySQLdb, random
db='memory2'

def rollback():
	print "CODE THIS!"

def origin():
	conn = gc_(); cur = conn.cursor()
	cur.execute("create table mem(element varchar(15), score float)")
	cur.execute("create table dump(element varchar(15), score float, times int)")
	cur.execute("create table _dump(element varchar(15), score float, times int)")
	conn.close()

def integrate(table, cur):
	backup()
	cur.execute("drop table mem")
	print "memory: mem forgotten"
	cur.execute("flush tables")
	cur.execute("truncate dump")
	cur.execute("insert into dump select * from "+table)
	print "memory: tables flushed"
	cur.execute("rename table "+table+" to mem")
	cur.execute("alter table mem drop column times")
	print "memory: new memory made"
	
def control(_int):
	conn = gc_(); cur = conn.cursor(); name=''
	if _int is 0: #create table _tempXXXX(element varchar(15), score float, times int)
		name = '_temp'+str(random.randint(1000, 9999))
		cur.execute("create table "+name+"(element varchar(15), score float, times int)")
	if _int is 1:
		name = '_mem'+str(random.randint(1000, 9999))
		cur.execute("create table "+name+" like mem")
	if int is 2: cur.execute("create table dump(element varchar(15), score float, times int)")
	conn.close()
	return name

def c_(command):
	conn = gc_(); cur = conn.cursor()
	cur.execute(command)
	conn.close()

def gc_():		
	return MySQLdb.connect(user='root', passwd='aditya', db=db)	

def recollect():
	conn = gc_(); cur = conn.cursor()
	cur.execute("select * from mem"); conn.close()
	return {e[0]: e[1] for e in cur.fetchall()}

def backup():
	conn = gc_(); cur = conn.cursor()
	cur.execute("insert into "+control(1)+" select * from mem")

def forget(name):
	c_("drop table "+name)

def death():
	c_("drop database "+db)
"""
Master tables:
1) mem(element varchar(15), score float)
2) _mem**** [previous iterations of mem]

"""	