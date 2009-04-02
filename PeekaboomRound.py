from pyparsing import nestedExpr
from PeekaboomEvent import *
import copy

class PeekaboomRound():
  """
    Represents one round of play: an exchange between a peek player and a boom player concerning a single object. A PeekaboomRound is initialized with one line of data from a .pkb file. The initializer parses the line and assigns properties to the PeekaboomRound instance accordingly.
    
    Events are stored as PeekaboomEvents, and blob events can be accessed independently with the blobs() method. The Point2 objects (from the euclid module) associated with those blob events can be accessed with blobPoints(), and a PointCluster object can be generated from those points with the cluster() method.
    
    The merge() method is used to non-destructively join multiple PeekaboomRound objects into a single object. The resulting object ends up representing the events from multiple rounds of play and is useful for initializing a Photographer object with all the data for a particular label in an image.
  """
  
  def __init__(self, data):
    """takes a single line from a .pkb file"""
    data = nestedExpr().parseString( "(" + data + ")" ).asList()[0]
    self.typeOfPlay = data[0][0]
    self.imageID = data[1][0][0]
    self.label = data[1][1][0]
    self.startTime = data[2][0]
    self.imageWidth = int(data[3][0])
    self.imageHeight = int(data[3][1])
    # self.peekPlayerID = int(data[4][data[4].index("p") + 1])
    # self.boomPlayerID = int(data[4][data[4].index("b") + 1])
    self.events = []
    for eventData in data[5]:
      event = PeekaboomEvent(eventData)
      self.events.append(event)
  
  def blobs(self):
    """returns a list of blob events"""
    return filter((lambda x: x.kind == 'b'), self.events)
  
  def blobPoints(self):
    """returns a list of points from all blob events"""
    return map((lambda x: x.point), self.blobs())
  
  def cluster(self):
    """returns a PointCluster of self.blobPoints()"""
    return PointCluster(self.blobPoints())
    
  def merge(self, others):
    """takes other PeekaboomRounds and returns a new PeekaboomRound with properties of this one and the events from all"""
    merged = copy.deepcopy(self)
    if not isinstance(others,list):
      others = [others]
    for other in others:
      for event in other.events:
        merged.events.append(copy.deepcopy(event))
    return merged