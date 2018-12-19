import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from linearMotionFunctions import moveSinglePoint3D as moveSinglePoint

""" Move a point, 2D """
#-- Variables
songLength = 60*4+10    # piece length in seconds
stepsPS = 100           # steps per second

startX = -100           # move from startX, startY, startZ -> endX, endY, endZ
endX = 50
startY = -100
endY = 100
startZ =1
endZ = 9

#-- Initial Calculations
steps = songLength*stepsPS          # total number of steps
intervalM = songLength/steps        # seconds per step

s = np.array([startX,startY,startZ]) # starting point
start = np.reshape(s,(1,len(s)))

deltaX = (endX - startX)/steps      # change in X per step
deltaY = (endY - startY)/steps      # change in Y per step
deltaZ = (endZ - startZ)/steps      # change in Z per step

# Initial Position
initialPos = moveSinglePoint(start, deltaX,deltaY,deltaZ,1)

#-- Generate all steps

graphPoints = np.fromfunction(
                                lambda i,j:
                                moveSinglePoint(   np.array(initialPos),
                                        deltaX,
                                        deltaY,
                                        deltaZ,
                                        i),
                                (steps,1),
                                dtype=int
                                )
graphPoints = graphPoints[0]

fig = plt.figure()
ax = fig.add_subplot(111,
                    autoscale_on=False,
                    xlim=(startX,endX),
                    ylim=(startY,endY),
                    zlim=(0,10),
                    projection='3d')
ax.grid()
line, = ax.plot([],[],[],'o',lw=2,c='xkcd:coral')

def init():
    line.set_data([],[])
    line.set_3d_properties([])
    return line, #time_text

def animate(i):
    pointI = graphPoints[i]
    line.set_data(pointI[0],pointI[1])
    line.set_3d_properties(pointI[2])
    return line, #time_text

ani = animation.FuncAnimation(  fig, animate, np.arange(1,len(graphPoints)),
                                interval=intervalM,#intervalM*0.0002,
                                blit=True, init_func=init)
#ani.to_html5_video(embed_limit=None)
#ani.save("movingPoint.mp4")
plt.show()
