from math import*

class onePoint: 
	def __init__(self, x, y, name=None):
		self.x = int(x)
		self.y = int(y)
		self.name = name

def manhattan_distance(a, b):
    return (abs(a.x - b.x) + abs(a.y - b.y))


def readFile():
	coordList = []
	try:
		fp = open('input.txt', 'r')
		line = fp.readline().strip()
		counter = 0
		while line:
			coords = line.split(", ")
			coordList.append(onePoint( x=coords[0], y=coords[1], name=counter))
			counter += 1
			line = fp.readline().strip()
			
		return coordList
	finally:
		fp.close()

def maxX(cordList):
	return max(cordList, key=lambda point:point.x).x

def maxY(cordList):
	return max(cordList, key=lambda point:point.y).y

def minX(cordList):
	return min(cordList, key=lambda point:point.x).x

def minY(cordList):
	return min(cordList, key=lambda point:point.y).y

cordList = readFile()

localMaxX = maxX(cordList)
localMaxY = maxY(cordList)

localMinX = minX(cordList)
localMinY = minY(cordList)

print ("{}, {}".format(localMinX, localMinY))
print ("{}, {}".format(localMaxX, localMaxY))

spotsForPoint = {}
infinitePoints = []
counter = 0

for x in range(localMinX, localMaxX +1):
	for y in range(localMinY, localMaxY+1):
		thisSpot = onePoint(x, y)
		distList = []
		totalDistance = 0
		for z in cordList:
			dist = manhattan_distance(thisSpot, z)
			distList.append((dist, z))
			totalDistance += dist

		if totalDistance < 10000:
			counter += 1

		theMin = min(distList, key=lambda distPair:distPair[0])
		howMany = len([aPair for aPair in distList if aPair[0] == theMin[0]])
		if howMany == 1:
			closest = theMin[1].name
			spotsForPoint[closest] = spotsForPoint.get(closest, 0) +1
			if x == localMinX or x == localMaxX or y == localMinY or y == localMaxY:
				# we're on an edge.  Any solutions we found on that edge are infinities
				if not closest in infinitePoints:
					infinitePoints.append(closest)

theMax = 0
for a in cordList:
	countOfThis = spotsForPoint[a.name]
	if (a.name in infinitePoints):
		print("{}: infinite".format(a.name))
	else:
		print ("{}: {}".format(a.name, countOfThis))
		if countOfThis > theMax:
			theMax = countOfThis

print(theMax)
print(counter)