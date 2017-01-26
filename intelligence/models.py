import progressbar, learn, tools, memory

def _exec():
	sequence()
	model0()
	
def sequence():
	reload(learn)
	reload(memory)

def model0():
	'''
	Version 0
	The most basic thing I can think of
	Read the whole directory and scan reviews
	Include negation and emoticon testing (latter is redundant)
	Average out scores
	Find standard deviation and remove band (mean-sigma, mean+sigma) (modify later)
	'''
	bar = progressbar.ProgressBar()
	data = tools.loaddir("/home/aditya/Desktop/project/aclImdb/train/pos/")
	data.extend(tools.loaddir("/home/aditya/Desktop/project/aclImdb/train/neg/"))
	print "model: BEGIN"
	print "model: "+"reading data and scores"
	reviews=[]; scores=[]
	for w in bar(data):
		reviews.append(open(w[0]).read())
		scores.append(w[1])
	print "model: "+"read complete. now learning"
	bar = progressbar.ProgressBar()
	learn.learn(reviews, scores, bar=bar, verbose=True)
	
	print "model: learnt. now reviewing"
	connection = memory.gc_()
	cur = connection.cursor()
	cur.execute("insert into _dump select * from dump")
	print "model: dump backed up"
	cur.execute("select @av:= avg(times) from dump")
	cur.execute("delete from dump where times < @av")
	cur.execute("select @lim:=times from dump where element = 'good'")
	cur.execute("delete from dump where times > @lim")
	print "model: average filtering done"
	cur.execute(r"delete from dump where element like '%\'%\'%'")
	cur.execute(r"delete from dump where element like '%\'%' and element  not like '%n\'t%';")
	print "filtering complete. closing connection"
	connection.commit()
	connection.close()

#def test(testdir):


#def failure():

	