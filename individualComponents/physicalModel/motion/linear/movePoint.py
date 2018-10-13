import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from mpl_toolkits.mplot3d import Axes3D

""" Move a point, 2D """
songLength = 60*4 #seconds
stepsPS = 100 # steps per second
steps = songLength*stepsPS
intervalM = songLength/steps

startX = -100
endX = 100
startY = -100
endY = 100

s = np.array([startX,startY])#,0])
start = np.reshape(s,(1,len(s)))

deltaX = (endX - startX)/steps
deltaY = (endY - startY)/steps

def move(points, x, y,c):#, z,c):
    n = len(points)
    xmove = c*x*np.ones(n)
    ymove = c*y*np.ones(n)
    #zmove = c*z*np.ones(n)
    #move = np.array([xmove, ymove, zmove]).transpose()
    move = np.array([xmove, ymove]).transpose()
    out = points + move
    return(out)


rewinds = 4

#initialPos = move(start, deltaX,deltaY,deltaZ,-1*rewinds)
initialPos = move(start, deltaX,deltaY,1)


#-- Generate all steps

graphPoints = np.fromfunction(
                                lambda i,j:
                                move(   np.array(initialPos),
                                        deltaX,
                                        deltaY,
                                        #deltaZ,
                                        i),
                                (steps,1),
                                dtype=int
                                )
graphPoints = graphPoints[0]

fig = plt.figure()
ax = fig.add_subplot(111,
                    autoscale_on=False,
                    xlim=(startX,endX),
                    ylim=(startY,endY))#,
                    #projection='3d')
ax.grid()
line, = ax.plot([],[],'o-',lw=2,c='xkcd:coral')
time_template = 'time = %.1fs'
#time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    #time_text.set_text('')
    return line, #time_text

def animate(i):
    pointI = graphPoints[i]
    line.set_data(pointI[0],pointI[1])
    #time_text.set_text(time_template % (i*intervalM))
    return line, #time_text
ani = animation.FuncAnimation(  fig, animate, np.arange(1,len(graphPoints)),
                                interval=intervalM,#intervalM*0.0002,
                                blit=True, init_func=init)
plt.show()
