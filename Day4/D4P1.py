import re
import datetime
from enum import Enum

class OneNight:
	def __init__(self, guardID=None):
		self.guardID = guardID or None
		self.minutes = [0] * 60	


class State(Enum):
	asleep = "asleep"
	awake = "awake"

def extractDate(line):
	match = re.match('\[([0-9]*)-([0-9]*)-([0-9]*) ([0-9]*):([0-9]*)\]', line)
	return datetime.datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)))

def extractGuard(line):
	match = re.match('\[.*\] Guard #([0-9]*) begins shift', line)
	return int(match.group(1))
	

def readFile():
	operationHash = {}
	try:
		fp = open('input.txt', 'r')
		line = fp.readline().strip()
		while line:
			print(line)
			date = extractDate(line)
			if "Guard" in line:
				operationHash[date] = extractGuard(line)
			elif "wakes up" in line:
				operationHash[date] = State.awake
			elif "falls asleep" in line:
				operationHash[date] = State.asleep

			line = fp.readline().strip()
		return operationHash
	finally:
		fp.close()

def guardSleeping(guardID, startTime, endTime, newHash):
	newDate = startTime.replace(minute=0);
	if not newDate in newHash:
		newHash[newDate] = OneNight(guardID = guardID)

	for x in range(startTime.minute, endTime.minute):
		newHash[newDate].minutes[x] = 1

	print ("{}: {} - {} {}".format(guardID, startTime, endTime, newDate))

def rotateData(operationData):
	guardID = ''
	lastSleepTime = 0
	newHash = {}

	for key in sorted(operationData.keys()):
		time = key
		value = operationData[key]
		if value == State.awake:
			guardSleeping(guardID, lastSleepTime, key, newHash)
		elif value == State.asleep:
			lastSleepTime = key
		else:
			guardID = value

	return newHash

def prettyPrintHash(newHash):
	for x in sorted(newHash.keys()):
		thisLine = str(x) + ": " + str(newHash[x].guardID) + "\t"
		for y in range(60):
			if (newHash[x].minutes[y] == 0):
				thisLine += "."
			else:
				thisLine += "*"

		thisLine += "({})".format(countMinutesAsleep(newHash[x].minutes))
		print(thisLine)

def countMinutesAsleep(minuteList):
	minutesAsleep = 0
	for x in minuteList:
		if not x == 0:
			minutesAsleep+=1
	return minutesAsleep

def sumMinutesPerGuard(newHash):
	minuteGuardHash = {}
	for x in sorted(newHash.keys()):
		guardID = newHash[x].guardID
		if not guardID in minuteGuardHash:
			minuteGuardHash[guardID] = 0
		minuteGuardHash[guardID] += countMinutesAsleep(newHash[x].minutes)
	print (minuteGuardHash)
	maxGuardID = list(minuteGuardHash.keys())[0]

	for y in minuteGuardHash.keys():
		if (minuteGuardHash[y] > minuteGuardHash[maxGuardID]):
			maxGuardID = y

	print(maxGuardID)
	return maxGuardID

def findSleepiestMinute(newHash, guardID):
	minutesInHour = [0] * 60
	for x in newHash.keys():
		if not newHash[x].guardID == guardID:
			continue
		for y in range(60):
			minutesInHour[y] += newHash[x].minutes[y]

	sleepiestMinute = 0
	for z in range(60):
		if minutesInHour[z] > minutesInHour[sleepiestMinute]:
			sleepiestMinute = z

	print("Guard {}:\t{} {} ({})".format(guardID, sleepiestMinute, minutesInHour[sleepiestMinute], guardID * sleepiestMinute))
	return sleepiestMinute

def findSleepiestMinuteForAllGuards(newHash):
	guardList = []
	for x in newHash.keys():
		if not newHash[x].guardID in guardList:
			guardList.append(newHash[x].guardID)

	for y in guardList:
		findSleepiestMinute(newHash, y)



operationData = readFile()
newHash = rotateData(operationData)
prettyPrintHash(newHash)
sleepiestGuard = sumMinutesPerGuard(newHash)
sleepiestMinute = findSleepiestMinute(newHash, sleepiestGuard)
print(sleepiestGuard * sleepiestMinute)

findSleepiestMinuteForAllGuards(newHash)