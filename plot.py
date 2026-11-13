import fractals
import matplotlib.pyplot as plt
import numpy as np
import math

def plot(corners, centre):
    gen = fractals.Generator(corners, 0.5)

    points : list [fractals.Point] = []
    for i in range (1000):
        points.append(centre)
        centre = gen.generate(centre)

    # plot
    x = []
    y = []
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

centre = fractals.Point(0.5, math.sqrt(3)/4)

plot([c1,c2,c3,c4], centre)