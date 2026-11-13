import fractals
import matplotlib.pyplot as plt
import numpy as np
import math

def plot(corners : list[fractals.corners], centre : fractals.Point, iterations : int, plotsize : float) -> None:
    gen = fractals.Generator(corners, fractals.ratio(len(corners)))

    points : list [fractals.Point] = []
    for i in range (iterations):
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

    plt.scatter(x, y, s=plotsize)
    plt.show()



def takeN(n, iter, size):
    try:
        corners = fractals.corners(int(n))
        plot(corners, corners[0].coords, int(iter), int(size))
    except TypeError: pass
    