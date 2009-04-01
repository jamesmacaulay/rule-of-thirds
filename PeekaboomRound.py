from pyparsing import nestedExpr
from PeekaboomEvent import *
import copy

class PeekaboomRound():
  """represents one round of play: an exchange between a peek player and a boom player concerning a single object"""
  
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