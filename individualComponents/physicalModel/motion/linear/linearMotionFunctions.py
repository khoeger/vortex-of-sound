import numpy as np

def moveSinglePoint2D(points, x, y,c):
    n = len(points)
    xmove = c*x*np.ones(n)
    ymove = c*y*np.ones(n)
    move = np.array([xmove, ymove]).transpose()
    out = points + move
    return(out)
