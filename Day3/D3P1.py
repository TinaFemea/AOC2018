import re

def buildDictionary(list, dict):
	for a in list:
		if (a in dict):
			dict[a] += 1
		else:
			dict[a] = 1

def countConflicts(dict):
	count = 0
	for key, value in dict.items():
		if (value > 1):
			count += 1
	return count

def buildListOfTuples(line):
	tupleList = []

	match = re.match('#([0-9]*) @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)', line)
	rowID = match.group(1)
	xOrigin = int(match.group(2))
	yOrigin = int(match.group(3))
	width = int(match.group(4))
	height = int(match.group(5))

	for a in range(width):
		for b in range(height):
			tupleList.append((xOrigin + a, yOrigin + b))
			b += 1
		a+=1

	return tupleList

def readFile():
	entireDict = {}
	try:
		fp = open('input.txt', 'r')
		line = fp.readline().strip()
		while line:
			tupleList = buildListOfTuples(line)
			buildDictionary(tupleList, entireDict)
			line = fp.readline().strip()
		print(countConflicts(entireDict))
		return entireDict
	finally:
		fp.close()

def doesThisListHaveConflicts(list, dict):
	for a in list:
		if (dict[a] > 1):
			return True
	return False
			
def seeIfItConfilicted(entireDict):
	try:
		fp = open('input.txt', 'r')
		line = fp.readline().strip()
		while line:
			tupleList = buildListOfTuples(line)
			if not doesThisListHaveConflicts(tupleList, entireDict):
				print (line)
			line = fp.readline().strip()
	finally:
		fp.close()


theDict = readFile()
seeIfItConfilicted(theDict)