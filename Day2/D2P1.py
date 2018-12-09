def hasExactlyNDuplicates(stringHash, count):
	for value in stringHash.values():
		if (value == count):
			return True
	return False

def turnStringIntoHash(string):
	stringHash = {}
	for c in string:
		if (c in stringHash):
			stringHash[c] += 1
		else:
			stringHash[c] = 1
	return stringHash

def readFile():
	numTwos = 0
	numThrees = 0
	try:
		fp = open('input.txt', 'r')
		line = fp.readline().strip()
		while line:
			stringHash = turnStringIntoHash(line)
			print(stringHash)
			if (hasExactlyNDuplicates(stringHash, 2)):
				numTwos += 1
			if (hasExactlyNDuplicates(stringHash, 3)):
				numThrees += 1
			print("{} {}".format(numTwos, numThrees))
			line = fp.readline().strip()
		
		return numTwos * numThrees

	finally:
		fp.close()

print(readFile())