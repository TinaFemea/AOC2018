#!/usr/bin/python


def readFileOnce(total, numbersSeen):
	try:
		fp = open('input.txt', 'r')
		line = fp.readline().strip()
		while line:
			sign = line[0]
			number = int(line[1:])
			if (sign == '-'):
				total -= number
			else: 
				if (sign == '+'):
					total += number

			if (total in numbersSeen):
				print ("Seen Twice: {}".format(total))
				numbersSeen[total] += 1
				break
			else:
				numbersSeen[total] = 1

			#print("{}{} {}".format(sign, number, total))
			line = fp.readline().strip()
		return total
	finally:
		fp.close()

def haveISeenDuplicate(numbersSeen):
	for value in numbersSeen.values():
		if (value > 1):
			return True
	return False

numbersSeen = {}
total = 0

while not haveISeenDuplicate(numbersSeen):
	total = readFileOnce(total, numbersSeen)
	print (total)
