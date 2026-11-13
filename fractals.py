import random

class Point():
    x : float
    y : float

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, value):
        return (value.x == self.x) and (value.y == self.y) 
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)
    
    

class Corner():
    name : str
    coords : Point

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords


class Generator():
    corners : list[Corner]
    ratio : float ## unused right now

    def __init__(self, corners, ratio):
        self.corners = corners
        self.ratio = ratio

    def avg(self, p1 : Point, p2 : Point) -> Point:
        return Point((p1.x + p2.x)/2, (p1.y + p2.y)/2)
    

    def generate(self, last : Point) -> Point:
        other : Point = random.choice(self.corners).coords 
        return self.avg(last, other)