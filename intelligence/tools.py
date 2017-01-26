import os

def loaddir(path):
	files = os.listdir(path)
	return [(path+file, (file.split(".")[0]).split("_")[1]) for file in files]
