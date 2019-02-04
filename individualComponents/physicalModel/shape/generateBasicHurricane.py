import hurricaneEqns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# -- Basic Parabola Needs
n = 3*10**3                                         # n points
z_range = [0, 9.5]                                  # height of vortex
scalingFactor = 24/50                               # target vertex height of whole
r_range = [20, 100]                                 # width of outer reaches of vortex
vertex = [r_range[0], z_range[1] * scalingFactor]   # vertex of outer reaches of vortex
point = [r_range[1], z_range[1]]

# # Generate heights, thetas, p, radii
# heights = hurricaneEqns.chooseZ(z_range, n)
# thetas = hurricaneEqns.chooseTheta(n)
# p = hurricaneEqns.calculateP( point, scalingFactor)
# maxR = hurricaneEqns.maxRForZ( heights, vertex, p)
# rs = hurricaneEqns.chooseR(r_range[0], maxR)
#
# # in caretsian coordinages
# x = hurricaneEqns.polarToX(rs, thetas)
# y = hurricaneEqns.polarToY(rs, thetas)
# z = heights
# coords = np.array([x,y,z])
# # Transpose coordinates
# #coordsT = coords.transpose()

# -- Generate Hurricane
testV = hurricaneEqns.VortexShape(n, z_range, scalingFactor, r_range, vertex, point)
coordsT = testV.returnInitialVortex()
# -- Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.autoscale_view(tight=False)
ax.set_xscale("linear")
ax.set_yscale("linear")
ax.set_zscale("linear")
ax.set_zlim3d(bottom=0,top=15)
ax.relim()
ax.scatter( coordsT[:,0],#x ,
            coordsT[:,1],#y,
            coordsT[:,2],#z
            c = "xkcd:coral",
            marker = "o")
plt.show()
