import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

""" Move a point, 2D """
songLength = 1#60*4 #seconds
stepsPS = 10 # steps per second
steps = songLength*stepsPS
intervalM = songLength/steps

startX = -100
endX = 50
startY = -100
endY = 100
startZ =4
endZ = 9

s = np.array([  [startX,    startY,     startZ]     ,
                [2*startX,  2*startY,   2*startZ]   ])#,0])

if s.shape[0]==1:
    start = np.reshape(s,(1,s.shape[1]))
else:
    start = s

deltaX = (endX - startX)/steps
deltaY = (endY - startY)/steps
deltaZ = (endZ - startZ)/steps

def move(points, x, y, z, c):#, z,c):
    n = len(points)
    #print(n)
    xmove = c*x*np.ones(n)
    #print("c",c)
    #print("x",x)
    #print("xmove", len(xmove), xmove)
    ymove = c*y*np.ones(n)
    zmove = c*z*np.ones(n)
    m = np.array([xmove, ymove, zmove]).transpose()

    pointArray = np.array(
        [
            np.full(    (   points.shape[0], points.shape[1]),
                        points[point]   )
                    for point in range(points.shape[0])
        ]
    )
    #move = np.array([xmove, ymove]).transpose()
    print("points\n",points)
    print("dim points:", points.shape,"\n\n")
    print("points array\n",pointArray)
    print("dim points array:", pointArray.shape,"\n\n")
    print("m\n",m)
    print("dim m:", m.shape,"\n\n")
    out = pointArray + m
    print("out\n", out)
    print("dim out:", out.shape,"\n\n")
    return(out)
#print(move(start,deltaX,deltaY,deltaZ,1))

rewinds = 4

print("---\nInitial Position\n---")
initialPos = move(start, deltaX,deltaY,deltaZ,1)
#initialPos = move(start, deltaX,deltaY,1)
print(initialPos)

print("---\nGraph Points\n---")
#-- Generate all steps

graphPoints = np.fromfunction(
                                lambda i,j,k:
                                move(   np.array(initialPos),
                                        deltaX,
                                        deltaY,
                                        deltaZ,
                                        j),
                                (2,steps,3),
                                dtype=int
                                )

print("Graph Points")
#print(len(graphPoints))
#print(graphPoints[:,0])
print(graphPoints)
#
# fig = plt.figure()
# ax = fig.add_subplot(111,
#                     autoscale_on=False,
#                     xlim=(-200,200),
#                     ylim=(-200,200),
#                     zlim=(0,10),
#                     projection='3d')
# ax.grid()
# line, = ax.plot([],[],[],'o',lw=2,c='xkcd:coral')
# #time_template = 'time = %.1fs'
# #time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
#
# def init():
#     line.set_data([],[])
#     line.set_3d_properties([])
#     #time_text.set_text('')
#     return line, #time_text
#
# def animate(i):
#     print(i)
#     pointI = graphPoints[i]
#     #line.set_data(pointI[:,0],pointI[:,1])
#     #line.set_3d_properties(pointI[:,2])
#     pTranspose = pointI.T
#     print(pTranspose)
#     line.set_data(pTranspose[0],pTranspose[1])
#     line.set_3d_properties(pTranspose[2])
#     #time_text.set_text(time_template % (i*intervalM))
#     return line, #time_text
# ani = animation.FuncAnimation(  fig, animate, np.arange(1,len(graphPoints)),
#                                 interval=200,#intervalM,
#                                 blit=True, init_func=init)
# #ani.to_html5_video(embed_limit=None)
# #ani.save("movingPoint.mp4")
# plt.show()
