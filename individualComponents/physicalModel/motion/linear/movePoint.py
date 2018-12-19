import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

""" Move a point, 2D """
songLength = 60*4+10            # piece length in seconds
stepsPS = 100                   # steps per second
steps = songLength*stepsPS      # total number of steps
intervalM = songLength/steps    # seconds per step

startX = -100                   # move from startX, startY -> endX, endY
endX = 100
startY = -100
endY = 100

s = np.array([startX,startY])       # starting point
start = np.reshape(s,(1,len(s)))

deltaX = (endX - startX)/steps      # change in X per step
deltaY = (endY - startY)/steps      # change in Y per step

def move(points, x, y,c):
    n = len(points)
    xmove = c*x*np.ones(n)
    ymove = c*y*np.ones(n)
    move = np.array([xmove, ymove]).transpose()
    out = points + move
    return(out)

initialPos = move(start, deltaX,deltaY,1)

#-- Generate all steps

graphPoints = np.fromfunction(
                                lambda i,j:
                                move(   np.array(initialPos),
                                        deltaX,
                                        deltaY,
                                        i),
                                (steps,1),
                                dtype=int
                                )
graphPoints = graphPoints[0]

fig = plt.figure()
ax = fig.add_subplot(111,
                    autoscale_on=False,
                    xlim=(startX,endX),
                    ylim=(startY,endY))
ax.grid()
line, = ax.plot([],[],'o-',lw=2,c='xkcd:coral')
time_template = 'time = %.1fs'

def init():
    line.set_data([], [])
    return line,

def animate(i):
    pointI = graphPoints[i]
    line.set_data(pointI[0],pointI[1])
    return line,
ani = animation.FuncAnimation(  fig, animate, np.arange(1,len(graphPoints)),
                                interval=intervalM,
                                blit=True, init_func=init)
plt.show()
