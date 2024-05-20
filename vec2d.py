import math

class Vec2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return(f'({self.x}, {self.y})')

    def __len__(self):
        return math.sqrt(self.x*self.x+self.y*self.y)
    
    __abs__ = __len__

    def __add__(self,other):
        return Vec2d(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vec2d(self.x-other.x,self.y-other.y)

    def __mul__(self,other):
        if isinstance(other,Vec2d):
            return Vec2d(self.x*other.x,self.y*other.y)
        elif isinstance(other,int) or isinstance(other,float):
            return Vec2d(self.x*other,self.y*other)

    def __truediv__(self,other):
        if isinstance(other,Vec2d):
            return Vec2d(self.x/other.x,self.y/other.y)
        elif isinstance(other,int) or isinstance(other,float):
            return Vec2d(self.x/other,self.y/other)

    def normalised(self):
        if abs(self)==0:
            return Vec2d(0,0)
        return self/abs(self)
    
    def normalise(self):
        normalised = self.normalised()
        self.x = normalised.x
        self.y = normalised.y

    def rotate(self,a):
        a = math.radians(a)
        len = round(abs(self),4)
        self.x = round(math.cos(a),4) * len
        self.y = round(math.sin(a),4) * len
        return self

    def angle(self):
        return math.degrees(math.atan2(self.y,self.x))