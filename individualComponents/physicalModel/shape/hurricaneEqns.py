import numpy as np

def calculateP( point, scalar):
    """ return the hurricane's p value"""
    numerator = point[1]*(1-scalar)
    denominator = 4 * point[0]
    return(numerator **2 /denominator)

def chooseZ( zrange , n ):
    """ choose n uniform random z value """
    outZs = np.random.uniform( zrange[0], zrange[1], n)
    return(outZs)

def maxRForZ( zValue, vertex, p ):
    """ calculate the maximum radius/parabola radius at a particular height"""
    numerator = (zValue - vertex[1])
    numerator = np.square(numerator)
    denominator = 4 * p
    out = numerator/denominator + vertex[0]
    return(out)

def chooseR( rmin, rmax):
    """ choose a uniform random radius r given rmin and rmax """
    r = np.random.uniform(rmin,rmax)
    return(r)

def chooseTheta(n):
    """ choose a random uniform theta, [0,2pi] """
    outThetas = np.random.uniform(0, 2*np.pi,n)
    return(outThetas)

def polarToX ( r , theta ):
    return(r*np.cos(theta))

def polarToY ( r , theta ):
    return(r*np.sin(theta))

class VortexShape():
    """ Class that creates a basic Vortex object"""
    def __init__(self,
                n,
                z_range,
                scalingFactor,
                r_range,
                vertex,
                point ):
        #-- define constants
        self.n = n
        self.zRange = z_range
        self.scalar = scalingFactor
        self.rRange = r_range
        self.v = vertex
        self.pt = point
    #-- Generate heights, thetas, p, radii
    #def genPointInfo(self):
        self.heights = chooseZ(self.zRange, self.n)
        self.thetas = chooseTheta(self.n)
        self.pVal = calculateP( self.pt, self.scalar)
        self.maxR = maxRForZ( self.heights, self.v, self.pVal)
        self.rs = chooseR(self.rRange[0], self.maxR)
        self.x = polarToX(self.rs, self.thetas)
        self.y = polarToY(self.rs, self.thetas)
        self.z = self.heights
        self.coords = np.array([self.x, self.y, self.z])
        self.coordsT = self.coords.transpose()
    def returnInitialVortex(self):
        return(self.coordsT)

class leveledVortexShape():
    """ Create a leveled vortex """
    def __init__(self,
                n,
                z_range,
                scalingFactor,
                r_range,
                vertex,
                point,
                #num_levels,
                level_proportions,
                level_bottom_heights ):
        #-- define constants
        self.n = n
        self.zRange = z_range
        self.scalar = scalingFactor
        self.rRange = r_range
        self.v = vertex
        self.pt = point
        self.lProportions = level_proportions
        self.bHeights = level_bottom_heights
        self.nLevels = len(level_proportions)

    #-- Generate heights, the
