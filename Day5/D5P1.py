
def readFileIntoList():
	try:
		fp = open('input.txt', 'r')
		line = fp.read().strip()
		return list(line)
	finally:
		fp.close()

def getRidOfReaction(theList):
	foundSomething = True
	while foundSomething:
		foundSomething = False
		for x in range(len(theList)-1):
			if (theList[x].swapcase() == theList[x+1]):
				del theList[x:x+2]
				foundSomething = True
				break
	print(len(theList))
	return len(theList)

def findAllUniques(theList):
	newList = []
	for x in range(len(theList)):
		lower = theList[x].lower()
		if not lower in newList:
			newList.append(lower)
	return (newList)


theList = readFileIntoList()
toBeRemoved = findAllUniques(theList)

theMax = len(theList)
theLetter = ""
for x in toBeRemoved:
	tempList = list(filter(lambda a: a != x and a != x.upper(), theList))
	numLeft = getRidOfReaction(tempList)
	if (numLeft < theMax):
		theMax = numLeft
		theLetter = x

	print("{}: {}".format(x, numLeft))

print("Min: {} {}".format(theLetter, theMax))

#print (len(trimmedList))
#print("".join(trimmedList))