from PeekaboomRound import *
import math

class Photographer():
  """
    The Photographer class is initialized with a PeekaboomRound object
    and is responsible for evaluating a single object's adherence to
    the rule of thirds. This returned through the Photographer's
    ruleOfThirds() method as a value between 0.0 and 1.0.
    
     The Photographer considers the image to be squashed into a square;
    that is, (x,y) co-ordinates are always expressed by the
    Photographer as values between 0.0 and 1.0, where 1.0 is equal to
    the width or height of the image respectively. This is to ensure
    that proximities are evaluated relative to the image as a whole and
    that the focus is on the vertical and horizontal rhythms rather
    than absolute pixel values.
    
     The ruleOfThirds method ends up taking into account two different
    factors and returns a weighted average of them:
    
     The first factor is based on the clusterIsAlongLine() method,
    which checks the PeekaboomRound's cluster of points against one of
    the Photographer's gridlines and returns a value closer to 1.0 when
    the lengthAxis() of the PointCluster is both close in distance and
    similar in rotation to the gridline.
    
     The second factor is returned by the clusterIsAtPoint() method,
    which returns a value closer to 1.0 when the PointCluster is close
    in distance to a given intersection.
    
     The Photographer checks the output of clusterIsAlongLine() for
    each of the gridlines, and checks the output of clusterIsAtPoint()
    for each of the gridline intersections. Only the maximum of these
    two sets of values are considered, since the Photographer only
    cares about the gridline and/or intersection of best fit for the
    cluster.
    
     The return value of the PointCluster's elongation() method is then
    used as the balance for weighting the two maximums. This means
    that, for clusters of points which are more elongated, the
    Photographer will care more about the cluster being along a
    gridline than about its centre being close to one of the
    intersections.
    
     The Photographer's maxDistance property is the maximum distance
    for which one point can be considered "close to" another. The
    maxDistance property has been set to one ninth of the width/height
    of the image. Similarly, the maxRotation property is the maximum
    rotation for which a line can be considered at all "aligned with"
    another line, and it has been set to 30 degrees (pi/6 radians).
  """
  
  # max distance for a point to be near another one,
  # relative to picture size (e.g. as a multiple of picture dimensions)  
  maxDistance = 1./9. # ratio of image dimensions
  
  # max rotation between two lines, in radians, for
  # those lines to be "aligned"
  maxRotation = math.pi / 6.
  
  gridlines = [ \
    Line2(Point2(0., 1./3.), Vector2(1.,0.)), \
    Line2(Point2(0., 2./3.), Vector2(1.,0.)), \
    Line2(Point2(1./3., 0.), Vector2(0.,1.)), \
    Line2(Point2(2./3., 0.), Vector2(0.,1.))  \
  ]
  
  intersections = [ \
    Point2(1./3., 1./3.), \
    Point2(1./3., 2./3.), \
    Point2(2./3., 1./3.), \
    Point2(2./3., 2./3.)  \
  ]
  
  def __init__(self, peekaboomRound):
    self.peekaboomRound = peekaboomRound
  
  def relativeCluster(self):
    """returns a PointCluster from self.peekaboomRound transformed into relative co-ordinates between 0.0 and 1.0"""
    return PointCluster(map((lambda p: self.relativePoint(p)), self.peekaboomRound.cluster()))
  
  def ruleOfThirds(self):
    """returns a confidence value for the object of the PeekaboomRound adhering to the rule of thirds in the image"""
    lineMatches = map((lambda line: self.clusterIsAlongLine(line)), self.gridlines)
    maxLineMatch = max(lineMatches)
    
    pointMatches = map((lambda point: self.clusterIsAtPoint(point)), self.intersections)
    maxPointMatch = max(pointMatches)
    
    pointLineBalance = self.relativeCluster().elongation()
    return self.weightedAverage(pointLineBalance, maxPointMatch, maxLineMatch)
  
  def relativeRotationalAlignment(self, rotation):
    """takes a rotation in degrees and returns its inverse relativized value between 0 and maxRotation (return value goes up as rotation goes down)"""
    return self.squishUp(1.0 - self.relativize(rotation, 0.0, self.maxRotation))

  def relativeProximity(self, distance):
    """takes a distance and returns the inverse of its relatived value between 0 and maxDistance (return value goes up when distance goes down)"""
    return self.squishUp(1.0 - self.relativize(distance, 0.0, self.maxDistance))
  
  def relativize(self, var, extremeA, extremeB):
    """takes a variable and two extremes, and returns a relative value between 0.0 and 1.0 depending on where the variable is situated between the extremes"""
    minExtreme = min(extremeA, extremeB)
    maxExtreme = max(extremeA, extremeB)
    if (var >= maxExtreme):
      return 1.0
    elif (var <= minExtreme):
      return 0.0
    else:
      return (var - minExtreme) / (maxExtreme - minExtreme)
  
  def weightedAverage(self, balance, extremeA, extremeB):
    """
      inverse of relativize()
      
      returns a weighted average between two extremes where balance is between 0.0 and 1.0
    """
    difference = abs(extremeA - extremeB)
    offset = balance * difference
    return ((extremeA - offset), (extremeA + offset))[extremeA < extremeB]
  
  def clusterIsAtPoint(self, point):
    """returns a value between 0.0 and 1.0 representing how much the cluster is located at a particular point"""
    return self.relativeProximity(self.relativeCluster().centre().distance(point))
  
  def clusterIsAlongLine(self, line):
    """returns a value between 0.0 and 1.0 representing how much the cluster is located along a particular line"""
    cluster = self.relativeCluster()
    clusterAxis = cluster.lengthAxis()
    distanceToLine = self.relativeProximity(cluster.centre().distance(line))
    rotationalAlignment = self.relativeRotationalAlignment(self.rotationBetweenLines(line, clusterAxis))
    return min(rotationalAlignment,distanceToLine)
  
  def rotationBetweenLines(self, line, segment):
    """docstring for rotationBetweenLines"""
    v1 = line.v.normalized()
    v2 = segment.v.normalized()
    radians = math.acos(v1.dot(v2))
    if (radians > math.pi):
      radians = math.pi - (radians - math.pi)
    return radians
    
  def relativePoint(self, p):
    """takes in a point and returns a new point with co-ordinates between 0.0 and 1.0, relative to the image height and width"""
    width = self.peekaboomRound.imageWidth
    height = self.peekaboomRound.imageHeight
    x = self.relativize(p.x, 0.0, width)
    y = self.relativize(p.y, 0.0, height)
    return Point2(x,y)

  # def squishDown(v):
  #   """takes in a number between 0.0 and 1.0 and applies a log function which bunches the distribution towards 0.0"""
  #   newV = 11 - (v * 10)
  #   return 1.0 - math.log(newV,11)
  
  def squishUp(self,v):
    """takes in a number between 0.0 and 1.0 and applies a log function which bunches the distribution towards 1.0"""
    newV = (v * 10) + 1
    return math.log(newV,11)







