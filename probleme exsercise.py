"""
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2=coor2

    def distance(self):
        dis= (((self.coor2[0]-self.coor1[0])**2)+(self.coor2[1]-self.coor1[1])**2)**0.5
        return 'Distance between given coordinates is %0.2f' %dis
    def slope(self):
        s=(self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
        return 'Slop between given coordinates is %0.2f' %s
a=Line((12,2),(9,1))
print(a.distance())
print(a.slope())
"""

class Cylinder:
    pi=3.141
    def __init__(self, height=1, radius=1):
        self.h=height
        self.r=radius

    def volume(self):
        vol= Cylinder.pi*(self.r**2)*self.h
        return 'Volume :- %.3f' %vol
    def surface_area(self):
        sarea=(2*self.pi*self.r*self.h)+2*self.pi*self.r**2
        return 'Sureface Area :- %0.3f' %sarea
a=Cylinder(2,3)
print(a.volume())
print(a.surface_area())