from Math import *
from Utilitary import *

class Grain(object):
    """grain"""

    def __init__(self, location,id,speed,acc,mass):
        self.__location = location # location in a 2D plan
        self.__id = id #integer which is specific to each grain
        self.__speed = speed # in meter per sec
        self.__acc = acc # in meter per sec per sec
        self.__force = (0,0) #in newton
        self.__mass = mass
        self.__ij = (0,0)

    def getid(self):
        return self.__id

    def getloc(self):
        return self.__location

    def setij(self,pos):
        self.__ij = pos

    def getij(self):
        return self.__ij
    def forcext(self,g,b):
        "calculates the sum of external forces "
        self.__force = add_vv(self.__force,(0,-9.81*self.__mass))# adding the weight
        self.__force = add_vv(self.__force,friction(self.__speed,g,b)) #adding fluid friction


    def bounceonwall(self,wall,kraid,radius):
        """calculates the force applied by a wall on a grain"""
        loc = self.__location
        ds = wall.getds()
        seg = wall.getseg()
        ab = normalize(dotovect(seg[0],seg[1]))
        am = dotovect(seg[0],loc)
        proj = dotprod(ab,am)
        point = add_vv(seg[0],prodscve(proj,ab))
        extremite = add_vv(loc,prodscve(-radius,ds))
        delta = dotprod(dotovect(point,extremite),wall.getds())
        self.__force = add_vv(self.__force,prodscve(halfspring(delta,kraid),ds))

    def interaction(self,grain2,radius,kraid):
        p2 = grain2.getloc()
        u = dotovect(self.__location,p2)
        n = norm(u)
        delta = n-2*radius
        f = halfspring(delta,kraid)
        fv = prodscve(-f,normalize(u))
        self.__force = add_vv(self.__force,fv)

    def move(self,dt):
        self.__acc = prodscve(1/self.__mass,self.__force)
        self.__speed = add_vv(self.__speed, prodscve(dt,self.__acc) )
        self.__location = add_vv(self.__location, prodscve(dt,self.__speed) )
        self.__force = [0,0]





class Wall(object):
    """wall"""

    def __init__(self, segment, vectdS):
        self.__segment = segment
        self.__vectdS = vectdS

    def getseg(self):
        return self.__segment

    def getds(self):
        return self.__vectdS
