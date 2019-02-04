import hurricaneEqns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# -- Basic Parabola Needs
n = 10**3                                                # n points
z_range = [0, 9.5]                                       # height of vortex
scalingFactor = 24/50                                    # target vertex height of whole
r_range = [20, 100]                                      # width of outer reaches of vortex
vertex = [r_range[0], z_range[1] * scalingFactor]#5.4 ]  # vertex of outer reaches of vortex
point = [r_range[1], z_range[1]]

colorList = [   "xkcd:coral",
                "xkcd:orange",
                "xkcd:goldenrod",
                "xkcd:lime",
                "xkcd:aqua",
                "orchid"]
legendLabels = [    "percussion",
                    "walking bass",
                    "chords",
                    "melody",
                    "harmony",
                    "counterpoint"
                    ]

# Instrument % distribution breakdown
percentages =   [   0.15, # percussion
                    0.16, # basso continuo
                    0.15, # chords
                    0.2,   # melody
                    0.16, # harmony
                    0.18 # counterpoint
                ]

# instrument height bounds
lenPercentages = len(percentages)
zero = np.zeros(1)
bounds = np.arange(  lenPercentages  )   / (    lenPercentages -1   )
#bottom
bottomHeights = np.concatenate( (zero    ,  bounds) )[:-1] * z_range[1]
#top
topHeights = bounds * z_range[1]

# Generate Vortex
vortex = hurricaneEqns.leveledVortexShape(  n,
                                            scalingFactor,
                                            r_range,
                                            vertex,
                                            point,
                                            percentages,
                                            bottomHeights,
                                            topHeights )
coordsArrayT = vortex.returnInitialVortex()

# - Plot
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.autoscale_view(tight=False)
ax.set_xscale("linear")
ax.set_yscale("linear")
ax.set_zscale("linear")
ax.set_zlim3d(bottom=0,top=15)
ax.relim()

for levelNum in range(len(coordsArrayT)):
    level = coordsArrayT[levelNum]
    color = colorList[levelNum]
    print(color)

    ax.scatter(     level[:,0], #x
                    level[:,1], #y
                    level[:,2], #z
                    c=color,
                    marker = "o",
                    label = legendLabels[levelNum]
            )

plt.legend()
plt.show()
