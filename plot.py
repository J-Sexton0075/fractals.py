import fractals
import matplotlib.pyplot as plt
import numpy as np
import math

def plot(corners, centre):
    gen = fractals.Generator(corners, fractals.ratio(len(corners)))

    points : list [fractals.Point] = []
    for i in range (0):
        points.append(centre)
        centre = gen.generate(centre)

    # plot
    x = []
    y = []

    for i in corners:
        x.append(i.coords.x)
        y.append(i.coords.y)
    
    for i in points:
        x.append(i.x)
        y.append(i.y)

    x = np.array(x)
    y = np.array(y)

    plt.scatter(x, y, s=10)
    plt.show()



# define a shape
c1 = fractals.Corner("c1", fractals.Point(0, 0))
c2 = fractals.Corner("c2", fractals.Point(1, 0))
c3 = fractals.Corner("c3", fractals.Point(0.5, math.sqrt(3)/2))
c4 = fractals.Corner("c4", fractals.Point(0,1))
c5 = fractals.Corner("c5", fractals.Point(1,1))


# these points DO NOT make a pentagon btw hence it doesn't work in the slightest
u1 = fractals.Corner("u1", fractals.Point(1,1))
u2 = fractals.Corner("u2", fractals.Point(0.3090, 0.9511))
u3 = fractals.Corner("u3", fractals.Point(-0.8090, 0.5878))
u4 = fractals.Corner("u4", fractals.Point(-0.8090, -0.5878))
u5 = fractals.Corner("u5", fractals.Point(0.3090, -0.9511))

# centre doesn't need to be chosen, actually its better if I did this randomly 
centre = fractals.centre([u1])

plot([u1,u2,u3,u4,u5], centre)