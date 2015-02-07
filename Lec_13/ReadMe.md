# MIT 6.00SC | Lecture 13 | Some Basic Probability and Plotting Data #

## [Introduction ](https://www.youtube.com/watch?v=hGQw3KJ7i6Q&list=PLB2BE3D6CA77BB8F7#t=22) ##

In the last lecture, we had a error in our code, because the Random walk code, did not output correct value of small samples as we had manually checked.

The problem was in the `simWalks()` method, which used wrong arguments, we had used this:-

````
distances.append(walk(f, homer, numTrials))
````

But we should have used:-

````
distances.append(walk(f, homer, numSteps))
````

So the complete corrected code is:-

````
import random

class Location(object):
    def __init__(self, x,y):
        """x and y are float"""
        self.x = x
        self.y = y
    def move(self,deltaX,deltaY):
        """deltaX and deltaY are float"""
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self,other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2) ** 0.5
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
        def __init__(self):
            self.drunks = {}
        def addDrunk(self,drunk,loc):
            if drunk in self.drunks:
                raise ValueError('Duplicate Drunk')
            else:
                self.drunks[drunk] = loc
        def moveDrunk(self,drunk):
            if not drunk in self.drunks:
                raise ValueError('Drunk not in field')
            xDist,yDist = drunk.takeStep()
            self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
        def getLoc(self, drunk):
            if not drunk in self.drunks:
                raise ValueError('Drunk not in field')
            return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
    def __str__(self):
        return 'This drunk is named ' + self.name

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))
def simWalks(numSteps, numTrials):
    homer = Drunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances
def drunkTest(numTrials):
    for numSteps in [10, 100, 1000, 10000, 100000]:
    # for numSteps in [0,1]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print '  Mean =', sum(distances)/len(distances)
        print '  Max =', max(distances), 'Min =', min(distances)
                
homer = Drunk("homer")
origin = Location(0,0)
field = Field()
field.addDrunk(homer,origin)
print "walk(field,homer,10): ", walk(field,homer,10)

drunkTest(10)
````

The above problem of random walk will give different output every time you run it, also we cannot infer much from it. So these type of problem are called stochastic problems.

## [Role of RandomNess in computation ](https://www.youtube.com/watch?v=hGQw3KJ7i6Q&list=PLB2BE3D6CA77BB8F7#t=515) ##

If we consider Newtonian physics, it is very comforting. To ever cause there is a reaction. Everything is deterministic.

Then came [Copenhagen Doctrines](http://en.wikipedia.org/wiki/Copenhagen_interpretation), associated with quantum physics changed this deterministic view of the world. It argued that, 

> natural change is necessarily by way of indeterministic physically discontinuous transitions between discrete stationary states

One can make probabilistic statements of the form **"X is highly likely to happen"**, but not statement of the form **"X is certain to happen."** What they meant was, The world is Stochastic.

But Einstein and Schrodinger disagreed the [Copenhagen Doctrines](http://en.wikipedia.org/wiki/Copenhagen_interpretation).

These two have practically divided the physics world, and at the heart of it was **Causal Non Determinism**.

### Causal Non Determinism ###

Causal Non Determinism believed that not every event is based on the cause of a previous event. Which was disagree by Einstein and Schrodinger. Famously said by Einstein "God Does not play Dice."

### Predictive Non Determinism ###

Our inability to make measurement of the physical world makes it impossible to make prediction of the future. So basically this means, things are not unpredictable, it just looks unpredictable because we do not have enough information.


causal Non-determinism 11:20
predictive Non-determinism

Stochastic Process 14:50

[PyLab](matplotlib.sourceforge.net)



## Reference ##
### Links ###

1. [MIT OCW](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-13-some-basic-probability-and-plotting-data/)
2. [Lecture Code handout (PDF)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-13-some-basic-probability-and-plotting-data/MIT6_00SCS11_lec13.pdf)
3. [Lecture code (Py)](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-2/lecture-13-some-basic-probability-and-plotting-data/lec13.py)
4. [Install PyLab](../misc/ReadMe.md)

### Check Yourself ###
### What is a stochastic process? ###
### What makes two events independent? ###