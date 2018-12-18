import hurricaneEqns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# -- Basic Parabola Needs
n = 3*10**3               # n points
z_range = [0, 9.5]      # height of vortex
scalingFactor = 24/50
r_range = [20, 100]      # width of outer reaches of vortex
vertex = [r_range[0], z_range[1] * scalingFactor]#5.4 ]  # vertex of outer reaches of vortex
point = [r_range[1], z_range[1]]

# Generate heights, thetas
heights = hurricaneEqns.chooseZ(z_range, n)

thetas = hurricaneEqns.chooseTheta(n)

p = hurricaneEqns.calculateP( point, scalingFactor)
maxR = hurricaneEqns.maxRForZ( heights, vertex, p)
rs = hurricaneEqns.chooseR(r_range[0], maxR)

# in caretsian
x = hurricaneEqns.polarToX(rs, thetas)
y = hurricaneEqns.polarToY(rs, thetas)
z = heights
coords = np.array([x,y,z])
#Transpose!
coordsT = coords.transpose()

# -- Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.autoscale_view(tight=False)
ax.set_xscale("linear")
#ax.set_xlim3d(left=-100,right=100)
ax.set_yscale("linear")
#ax.set_ylim3d(bottom=-100,top=100)
ax.set_zscale("linear")
ax.set_zlim3d(bottom=0,top=15)
ax.relim()
#ax = fig.add_subplot(111)
#ax.scatter(coords[0], coords[1],c="r",marker="o")
ax.scatter( coordsT[:,0],#x ,
            coordsT[:,1],#y,#np.zeros(n) ,
            coordsT[:,2],#z ,
            c = "xkcd:coral",
            marker = "o")
plt.show()
