#Collins Wanga
#10/11/2022


#Planets class with constructor
class Planet:
    def __init__(self, iname, irad, im, idist):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist

#2 Simple accessor methods

def getName (self):
    return self.name

def getRadius(self):
    return self.radius

def getMass(self):
    return self.mass

def getDistance (self):
    return self.distance


#3 Additional accessor methods
def getVolume(self):
    v = 4/3 * math.pi *self.radius**3
    return v

def getSurfaceArea(self):
    sa = 4 * math.pi * self.radius**2
    return sa

def getDensity(self):
    d = self.mass / self.getVolume()
    return d

#4 Mutator method in the Planet Class
def setName (self, newname):
    self.name = newname

#5 The show method
def show (self):
    print(self.name)

#6 The __str__ method
def __str__(self):
    return self.name

#The Sun Class
import math
class Sun:
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp

    def getMass(self):
        return self.mass

    def __str__(self):
        return self.name

#The Solar System Class
class SolarSystem:
    def __init__(self,asun):
        self.thesun = asun
        self.planets = []

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def showPlanets(self):
        for aplanet in self.planets:

            print(aplanet)

#The Solar System with a hidden turtle

class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0, -height/2.0, width/2.0, height/2.0)

    def addPlanet (self, aplanet):
            self.planets.append(aplanet)

    def addSun (self, asun):
            self.thesun = asun

    def showPlanets (self):
        for aplanet in sel.planets:
            print(aplanet)

    def freeze (self):
        self.ssscreen.exitonclick()


#The Sun Class with visualization

class Sun:
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    #other methods as before

    def getXPos (self):
        return self.x
    def getYPos (self):
        return self.y
