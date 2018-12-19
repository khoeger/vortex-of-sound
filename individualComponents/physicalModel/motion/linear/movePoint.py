import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from linearMotionFunctions import moveSinglePoint2D as moveSinglePoint

""" Move a point, 2D """

#-- Variables
songLength = 60*4+10            # piece length in seconds
stepsPS = 100                   # steps per second

startX = -100                   # move from startX, startY -> endX, endY
endX = 100
startY = -100
endY = 100

#-- Initial Calculations
steps = songLength*stepsPS          # total number of steps
intervalM = songLength/steps        # seconds per step

s = np.array([startX,startY])       # starting point
start = np.reshape(s,(1,len(s)))

deltaX = (endX - startX)/steps      # change in X per step
deltaY = (endY - startY)/steps      # change in Y per step


#-- Move to start

initialPos = moveSinglePoint(start, deltaX,deltaY,1)

#-- Generate all steps

graphPoints = np.fromfunction(
                                lambda i,j:
                                moveSinglePoint(   np.array(initialPos),
                                        deltaX,
                                        deltaY,
                                        i),
                                (steps,1),
                                dtype=int
                                ) # graphPoints takes the function
                                  # moveSinglePoint and applies it over each
                                  # (i, j) pair over a shape (steps,1), where
                                  # the output becomes (1,steps,2). The 1 comes
                                  # from (steps, 1) and the 2 comes from
                                  # initialPosition's dimension (1,2)

graphPoints = graphPoints[0]      # For graphing purposes, and easy manipulation
                                  # Isolate's the column of steps
"""
print(initialPos, initialPos.shape)
print(graphPoints.shape)
print(graphPoints[:10])
"""

fig = plt.figure()
ax = fig.add_subplot(111,
                    autoscale_on=False,
                    xlim=(startX,endX),
                    ylim=(startY,endY))
ax.grid()
line, = ax.plot([],[],'o-',lw=2,c='xkcd:coral')
#time_template = 'time = %.1fs'

def init():
    line.set_data([], [])
    return line,

def animate(i):
    pointI = graphPoints[i]
    line.set_data(pointI[0],pointI[1])
    return line,

ani = animation.FuncAnimation(  fig,
                                animate,
                                np.arange(1,len(graphPoints)),
                                interval=intervalM,
                                blit=True,
                                init_func=init)
plt.show()
