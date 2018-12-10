import re
import datetime
from enum import Enum

class OneNight:
	guardID = ''
	minutes = [None] * 60

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

def guardSleeping(guardID, startTime, endTime):
	print ("{}: {} - {}".format(guardID, startTime, endTime))

def rotateData(operationData):
	guardID = ''
	lastSleepTime = 0

	for key in sorted(operationData.keys()):
		time = key
		value = operationData[key]
		if value == State.awake:
			guardSleeping(guardID, lastSleepTime, key)
		elif value == State.asleep:
			lastSleepTime = key
		else:
			guardID = value

#		print(type(value))

operationData = readFile()
rotateData(operationData)