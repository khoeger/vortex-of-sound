import hurricaneEqns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# -- Basic Parabola Needs
n = 10**2                                                # n points
z_range = [0, 9.5]                                       # height of vortex
scalingFactor = 24/50                                    # target vertex height of whole
r_range = [20, 100]                                      # width of outer reaches of vortex
vertex = [r_range[0], z_range[1] * scalingFactor]#5.4 ]  # vertex of outer reaches of vortex
point = [r_range[1], z_range[1]]

# Instrument % distribution breakdown
melody = 0.3
percussion = 0.25
countermelody = 0.15
bassocontinuo = 0.15
chords = 0.15
# instrument height bottom bounds
chordHeightB = 0
bassoHeightB = chordHeightB+ 0.2*z_range[1]
melHeightB = bassoHeightB + 0.2*z_range[1]
cMelHeightB = melHeightB + 0.4*z_range[1]

# calculate p
p = hurricaneEqns.calculateP( point, scalingFactor)

# -- Generate heights, thetas, radius per  instrument
# - percussion
percussionN = np.floor(percussion * n).astype(int)
percussionThetas = hurricaneEqns.chooseTheta(percussionN)
percussionHeights = np.zeros_like(np.arange(percussionN))
pMaxR = hurricaneEqns.maxRForZ( percussionHeights, vertex, p)
pRs = hurricaneEqns.chooseR(r_range[0], pMaxR)

# in caretsian
px = hurricaneEqns.polarToX(pRs, percussionThetas)
py = hurricaneEqns.polarToY(pRs, percussionThetas)
pz = percussionHeights
pcoords = np.array([px,py,pz])
pcoordsT = pcoords.transpose()

# - chord
chordN = np.floor(chords * n).astype(int)
chordThetas = hurricaneEqns.chooseTheta(chordN)
chordHeights = hurricaneEqns.chooseZ([chordHeightB,bassoHeightB], chordN)
chMaxR = hurricaneEqns.maxRForZ( chordHeights, vertex, p)
chRs = hurricaneEqns.chooseR(r_range[0], chMaxR)

# in caretsian
chx = hurricaneEqns.polarToX(chRs, chordThetas)
chy = hurricaneEqns.polarToY(chRs, chordThetas)
chz = chordHeights
chcoords = np.array([chx,chy,chz])
chcoordsT = chcoords.transpose()

# - basso continuo
bassoN = np.floor(bassocontinuo * n).astype(int)
bassoThetas = hurricaneEqns.chooseTheta(bassoN)
bassoHeights = hurricaneEqns.chooseZ([bassoHeightB,melHeightB], bassoN)
bMaxR = hurricaneEqns.maxRForZ( bassoHeights, vertex, p)
bRs = hurricaneEqns.chooseR(r_range[0], bMaxR)

# in caretsian
bx = hurricaneEqns.polarToX(bRs, bassoThetas)
by = hurricaneEqns.polarToY(bRs, bassoThetas)
bz = bassoHeights
bcoords = np.array([bx,by,bz])
bcoordsT = bcoords.transpose()

# - melody
melodyN = np.floor(melody * n).astype(int)
melodyThetas = hurricaneEqns.chooseTheta(melodyN)
melodyHeights = hurricaneEqns.chooseZ([melHeightB,cMelHeightB], melodyN)
mMaxR = hurricaneEqns.maxRForZ( melodyHeights, vertex, p)
mRs = hurricaneEqns.chooseR(r_range[0], mMaxR)

# in caretsian
mx = hurricaneEqns.polarToX(mRs, melodyThetas)
my = hurricaneEqns.polarToY(mRs, melodyThetas)
mz = melodyHeights
mcoords = np.array([mx,my,mz])
mcoordsT = mcoords.transpose()

# - countermelody
counterMelodyN = np.floor(countermelody * n).astype(int)
counterMelodyThetas = hurricaneEqns.chooseTheta(counterMelodyN)
counterMelodyHeights = hurricaneEqns.chooseZ([cMelHeightB,z_range[1]], counterMelodyN)
cmMaxR = hurricaneEqns.maxRForZ( counterMelodyHeights, vertex, p)
cmRs = hurricaneEqns.chooseR(r_range[0], cmMaxR)

# in caretsian
cmx = hurricaneEqns.polarToX(cmRs, counterMelodyThetas)
cmy = hurricaneEqns.polarToY(cmRs, counterMelodyThetas)
cmz = counterMelodyHeights
cmcoords = np.array([cmx,cmy,cmz])
cmcoordsT = cmcoords.transpose()


# - Plot
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
ax.scatter( pcoordsT[:,0],#x ,
            pcoordsT[:,1],#y,#np.zeros(n) ,
            pcoordsT[:,2],#z ,
            c = "xkcd:coral",
            marker = "o")
ax.scatter( chcoordsT[:,0],#x ,
            chcoordsT[:,1],#y,#np.zeros(n) ,
            chcoordsT[:,2],#z ,
            c = "xkcd:orange",
            marker = "o")
ax.scatter( bcoordsT[:,0],
            bcoordsT[:,1],
            bcoordsT[:,2],
            c = "xkcd:goldenrod",
            marker = "o")
ax.scatter( mcoordsT[:,0],
            mcoordsT[:,1],
            mcoordsT[:,2],
            c = "xkcd:lime",
            marker = "o")
ax.scatter( cmcoordsT[:,0],
            cmcoordsT[:,1],
            cmcoordsT[:,2],
            c = "xkcd:aqua",
            marker = "o")

plt.show()
