import progressbar, learn, tools, memory

def _exec():
	sequence()
	model("/home/aditya/Desktop/project/aclImdb/train/pos/")
	
def sequence():
	reload(learn)
	reload(memory)

def model(datadir):
	'''
	Version 0
	The most basic thing I can think of
	Read the whole directory and scan reviews
	Include negation and emoticon testing (latter is redundant)
	Average out scores
	Find standard deviation and remove band (mean-sigma, mean+sigma) (modify later)
	'''
	bar = progressbar.ProgressBar()
	data = tools.loaddir(datadir)
	data.extend(tools.loaddir("/home/aditya/Desktop/project/aclImdb/train/neg/"))
	print "model: BEGIN"
	print "model: "+datadir
	print "model: "+"reading data and scores"
	reviews=[]; scores=[]
	for w in bar(data):
		reviews.append(open(w[0]).read())
		scores.append(w[1])
	print "model: "+"read complete. now learning"
	bar = progressbar.ProgressBar()
	learn.learn(reviews, scores, bar=bar)
	learn.post()

#def test(testdir):


#def failure():

	