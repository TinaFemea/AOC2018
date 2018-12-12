import re

operationList = {}
result = ""

def processLine(line):
	match = re.match('Step ([A-Z]) must be finished before step ([A-Z]) can begin.', line)
	before = match.group(1)
	after = match.group(2)
	if not before in operationList:
		operationList[before] = []
	if not after in operationList:
		operationList[after] = []

	operationList[after].append(before)	

def readFile():
	try:
		fp = open('input.txt', 'r')
		line = fp.readline().strip()
		while line:
			processLine(line)
			line = fp.readline().strip()
			
	finally:
		fp.close()

def findNext():
	global result
	readList = sorted(list(filter(lambda x: len(operationList[x]) == 0, operationList)))
	if (len(readList) == 0):
		return None

	return readList

def removeStep(whichStep):
	for x in operationList:
		if (whichStep in operationList[x]):
			operationList[x].remove(whichStep)
	operationList.pop(whichStep)

readFile()

def findNextNotWorkingOn(taskList, workerList):
	if (taskList == None):
		return None
	for i in range(5):
		if (workerList[i] != None):
			taskList.remove(workerList[i][1])

	if len(taskList) == 0:
		return None
	else:
		return taskList

doneList = []
numElves = 5
time = 61

def tick(counter, workerList):
	for i in range(numElves):
		if (workerList[i] != None):
			timer = workerList[i][0] 
			if (timer > 1):
				workerList[i] = (timer-1, workerList[i][1])
			else:
				removeStep(workerList[i][1])
				doneList.append(workerList[i][1])
				workerList[i] = None	

	for i in range(numElves):
		if (workerList[i] == None):
			taskList = findNextNotWorkingOn(findNext(), workerList)
			nextTask = None
			if (taskList != None):
				#print(taskList)
				nextTask = taskList[0]
			if (nextTask != None):
				workerList[i] = ((time + ord(nextTask) - ord('A'), nextTask))
			else:
				workerList[i] = None

	prettyPrint = ""
	for i in range(numElves):
		if (workerList[i] == None):
			prettyPrint += "."
		else:
			prettyPrint += workerList[i][1]

	print(str(counter) + ": " + prettyPrint + " " + ''.join(doneList))

workerList = [None] * 5

counter = 0
while len(operationList) > 0:
	tick(counter, workerList)
	counter += 1

print (counter)
print(result)
print(''.join(doneList))
#print (operationList)