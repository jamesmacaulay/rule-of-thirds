from euclid import *

class PointCluster(list):
  """
    This is a special list type for Point2 objects from the euclid module. It is a subclass of the built-in Python list class, with accessor methods for geometric values useful for the Photographer.
  """

  def centre(self):
    """returns this cluster's average/centre point as a new Point2"""
    averages = [0.,0.]
    for p in self:
      averages[0] = averages[0] + p.x
      averages[1] = averages[1] + p.y
    return Point2((averages[0] / len(self)), (averages[1] / len(self)))
  
  def lengthAxis(self):
    """returns a LineSegment2 representing the most distant pair of points in this cluster"""
    maxSegment = None
    for i in range(0, len(self)):
      for j in range((i + 1), len(self)):
        thisSegment = LineSegment2(self[i], self[j])
        if (maxSegment == None or maxSegment.length < thisSegment.length):
          maxSegment = thisSegment
    return maxSegment
    
  def widthAxis(self):
    """returns a LineSegment2 perpendicular to self.lengthAxis(), spanning the width of the cluster at a point on the lengthAxis() halfway between the two furthest points' closest points on the lengthAxis()"""
    lengthAxis = self.lengthAxis()
    lengthAxisHalfway = self.__halfwayPoint(lengthAxis)
    
    furthestDistances = [0.0, 0.0]
    furthestPoints = [lengthAxisHalfway, lengthAxisHalfway]
    furthestConnections = [lengthAxisHalfway.connect(lengthAxis), lengthAxisHalfway.connect(lengthAxis)]
    for point in self:
      if not((point == lengthAxis.p1) or (point == lengthAxis.p2)):
        side = self.__sideOfLine(point, lengthAxis)
        thisConnection = point.connect(lengthAxis)
        thisDistance = thisConnection.length
        if thisDistance >= furthestDistances[side]:
          furthestPoints[side] = point
          furthestDistances[side] = thisDistance
          furthestConnections[side] = thisConnection
    
    intersectionSpan = LineSegment2(furthestConnections[0].p2, furthestConnections[1].p2)
    intersectionSpanHalfway = LineSegment2(intersectionSpan.p1, (intersectionSpan.v / 2)).p2
    
    endpoints = []
    for i in [0,1]:
      endpoints.append(LineSegment2(intersectionSpanHalfway, (furthestConnections[i].v * -1)).p2)
    
    return LineSegment2(*endpoints)
  
  def elongation(self):
    """returns between 0.0 and 1.0 proportional to how elongated the cluster is"""
    if self.widthAxis().length == 0:
      return 1.0
    else:
      return min(1.0, (self.widthAxis().length / self.lengthAxis().length))
  
  def __halfwayPoint(self, segment):
    """takes a LineSegment2 and returns its halfway point"""
    return LineSegment2(segment.p1, (segment.v / 2)).p2
  
  def __sideOfLine(self, point, segment):
    """takes a Point2 and a LineSegment2 and returns 0 if the point is on one side of the line and 1 if it's on the other"""
    second_step = segment.p2.connect(point)
    return int(segment.v.cross().dot(second_step.v) > 0)