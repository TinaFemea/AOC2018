def readFile():
	listOfLines = []
	try:
		fp = open('input.txt', 'r')
		line = fp.readline().strip()
		while line:
			listOfLines.append(line)
			line = fp.readline().strip()
		
		return listOfLines

	finally:
		fp.close()

def isOffByOne(a, b):
	numDiffs = 0;
	for i in range(len(a)):
		if (a[i] != b[i]):
			numDiffs += 1
	#print(numDiffs)
	return numDiffs == 1


def findOneOffs(listOfLines):
	for a in listOfLines:
		for b in listOfLines:
			if isOffByOne(a, b):
				print(a, b)

listOfLines = readFile()
findOneOffs(listOfLines)