from PointCluster import *

class PeekaboomEvent():
  """
    Represents an event in a PeekaboomRound. Should not be initialized
    by the user.
  """
  
  def __init__(self, data):
    """takes a data list produced by PeekaboomRound"""
    self.timestamp = int(data[0][0])
    self.player = data[0][1]
    self.kind = data[1][0][0]
    self.point = None
    self.guess = None
    self.hint = None
    if self.player == 'b' and self.kind == 'p':
      self.kind = 'b'
    if self.kind == 'b':
      self.point = Point2(int(data[1][1][0]), int(data[1][1][1]))
    elif self.kind == 'g':
      self.guess = data[1][1][0]
    elif self.kind == 'h':
      self.hint = data[1][1][0]
    