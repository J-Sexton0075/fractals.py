import random
import math

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

    def __init__(self, corners : list[Corner], ratio : float):
        self.corners = corners
        self.ratio = ratio

    def avg(self, p1 : Point, p2 : Point) -> Point:
        return Point((p1.x + p2.x) * (1- self.ratio), (p1.y + p2.y) * (1-self.ratio))
    

    def generate(self, last : Point) -> Point:
        other : Point = random.choice(self.corners).coords 
        return self.avg(last, other)

# returns the ideal ratio for any N sided polygon
def ratio(n : int) -> float:
    # using the modular arithmetic method
    if (n % 4 == 0):
        return 1/(1+math.tan(math.pi/n))
    elif (n % 4 == 1 or n % 4 == 3):
        return 1/(1 + 2*math.sin(math.pi/(2*n)))
    else:
        return 1/(1 + math.sin(math.pi/n))
        

# returns the centrepoint (mean) of a collection of points
def centre(corners : list[Corner]):
    sumx = 0
    sumy = 0
    for i in corners:
        sumx += i.coords.x
        sumy += i.coords.y
    return Point(sumx/len(corners), sumy/len(corners))


def corners(n : int) -> list[Corner]:
    corners = []
    angle = (2 * math.pi) / n
    for i in range(0, n):
        x = math.cos(i * angle)
        y = math.sin(i * angle)
        corners.append(Corner("corner", Point(x,y)))
    return corners