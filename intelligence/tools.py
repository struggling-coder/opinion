import os, re

def loaddir(path):
	files = os.listdir(path)
	return [(path+file, (file.split(".")[0]).split("_")[1]) for file in files]

def ofscore(score):
	return filter(bool, [re.search(".[_]"+str(score)+".txt", e) for e in os.listdir(r"/home/aditya/Desktop/project/aclImdb/train/neg/")])
