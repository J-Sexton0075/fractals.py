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
    

class Corner():
    name : str
    coords : Point

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords


class Generator():
    corners : int
    ratio : float

    def __init__(self, corners, ratio):
        self.corners = corners
        self.ratio = ratio

    def generate(self, lastdigit):
        pass
