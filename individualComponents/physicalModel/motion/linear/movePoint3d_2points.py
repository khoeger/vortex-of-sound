import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

""" Move a point, 2D """

#-- Variables
songLength = 60*4 +10 # piece length in seconds
stepsPS = 100         # steps per second

startX = -200         # move from start(X,Y,Z) --> end(X,Y,X)
endX = 180
startY = -200
endY = 180
startZ =0
endZ = 9.5

pts = 10                # number of points moving

#-- Initial Calculations
steps = songLength*stepsPS      # total number of steps
intervalM = songLength/steps    # seconds per step

deltaX = (endX - startX)/steps      # change in X per step
deltaY = (endY - startY)/steps      # change in Y per step
deltaZ = (endZ - startZ)/steps      # change in Z per step

# Generate pts random starting points
genX = np.random.randint( low = -200, high = -150, size=(pts,1))
genY = np.random.randint( low = -200, high = -150, size=(pts,1))
genZ = np.random.rand(pts,1)*9
xy = np.append(genX, genY)
xyz = np.append(xy, genZ)
xyzThree = np.reshape(xyz,(3,pts))
s = xyzThree.T #Shape (pts,3)

print(s.shape)
if s.shape[0]==1:
    start = np.reshape(s,(1,s.shape[1]))
else:
    start = s

def move(points, x, y, z, c):
    n = len(points)
    xmove = c*x*np.ones(n)
    ymove = c*y*np.ones(n)
    zmove = c*z*np.ones(n) #+ np.random.randn(n)
    m = np.array([xmove, ymove, zmove]).transpose()
    out = points + m
    return(out)

# Generate all steps for each point
initialPos = move(start, deltaX,deltaY,deltaZ,1)

graphPoints = np.fromfunction(
                                lambda i,j,k:
                                move(   np.array(initialPos),
                                        deltaX,
                                        deltaY,
                                        deltaZ,
                                        j),
                                (1,steps,1),
                                dtype=int
                                )

# Graph points returns something of the shape (2,steps,3,pts)
# both of the columns in the first axis will return the same entries
# Use graphPoints[0] as input for allself.

# -- To Do: figure out how to run through without making the 2nd column --

fig = plt.figure()
ax = fig.add_subplot(111,
                    autoscale_on=False,
                    xlim=(-200,200),
                    ylim=(-200,200),
                    zlim=(0,10),
                    projection='3d')
ax.grid()
line, = ax.plot([],[],[],'o',lw=2,c='xkcd:coral')

def init():
    line.set_data([],[])
    line.set_3d_properties([])
    return line,

def animate(i):
    pointI = graphPoints[0][i]
    pTranspose = pointI.T
    line.set_data(pTranspose[0],pTranspose[1])
    line.set_3d_properties(pTranspose[2])
    return line,
ani = animation.FuncAnimation(  fig, animate, np.arange(1,len(graphPoints[0])),
                                interval=intervalM,
                                blit=True, init_func=init)
#ani.to_html5_video(embed_limit=None)
#ani.save("movingPoints.mp4")
plt.show()
print("Done!")
