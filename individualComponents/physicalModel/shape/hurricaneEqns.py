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
