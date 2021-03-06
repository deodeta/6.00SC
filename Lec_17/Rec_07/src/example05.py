import math
import random
import pylab

#####
# 
# Computing Pi
# 
# Square with 2r length Sides
# Inscribe circle with radius r
# Area of square = (2r)*2 = 4r^2
# Area of circle = pi*r^2
# Ratio of circle area to sqare area is (pi*r^2)/(4r^2) = pi/4
#
# Implication: Of N random points picked from inside square, N*pi/4
# will be inside circle
#
# So if M = number of points inside circle
# M = N*pi/4
# pi = M/N * 4


def randomPoints(r):
    x = random.uniform(-r,r)
    y = random.uniform(-r,r)
    return (x,y)

def makePoints(r,n):
    """
    Make n random points inside square with 2*r side.
    """    
    points = []
    for i in range(n):
        points.append(randomPoints(r))
    return points

def inCircle(r,points):
    x = points[0]    
    y = points[1]

    return x ** 2 + y ** 2 <= r ** 2

def numInCircle(r,points):
    """
    Figure out no of points inside circle of radius r
    """    
    count = 0
    for point in points:
        if inCircle(r,point):
            count += 1
    return count

def computePi(numPoints,points = None):
    """
        Computes Pi using Monte Carlo simulation of n points 
    """ 
    if points is None:
        points = makePoints(1.0,numPoints)
    inCircle = numInCircle(1.0, points)
    return float(inCircle)/float(numPoints) * 4.0

def runTrails(numTrailsPerPoints,numPointsList):
    results = []    
    for numPoints in numPointsList:
        print numPoints
        for trails in range(numTrailsPerPoints):
            results.append((numPoints,computePi(numPoints)))
    return results

def plotPi(trails,trailsResults):    
    numPoints = []
    results = []
    for result in trailsResults:
        numPoints.append(result[0])
        results.append(result[1])

    pylab.figure()
    pylab.clf()
    pylab.scatter(numPoints, results, c="r")
    pylab.plot(trails,[math.pi for trails in trails], c="b")
    pylab.xlabel("Number of Points")
    pylab.ylabel("Pi")
    pylab.title("Pi Vs Number of Points")
    pylab.show()

numTrailsPerPoints = 50
numPointsList = range(10,10000,1000)    
trailsResults = runTrails(numTrailsPerPoints, numPointsList)
plotPi(numPointsList, trailsResults)