import unittest
import fixtures
from PeekaboomRound import *

class PeekaboomRoundTestCase(unittest.TestCase):
  
  def setUp(self):
    self.cluster = PeekaboomRound(fixtures.roundData)
  
  def test_init(self):
    self.assertEqual('n', self.cluster.typeOfPlay)
    self.assertEqual('0a0a5415f77f3cc0177278c9a4401661', self.cluster.imageID)
    self.assertEqual('ocean', self.cluster.label)
    self.assertEqual('21.16.1.2.7.2005', self.cluster.startTime)
    self.assertEqual(297, self.cluster.imageWidth)
    self.assertEqual(212, self.cluster.imageHeight)
    # self.assertEqual(16035888797995720969136800, self.cluster.peekPlayerID)
    # self.assertEqual(477870931283701680717739166, self.cluster.boomPlayerID)
    self.assertEqual(37, len(self.cluster.events))
    self.assertEqual(2562, self.cluster.events[0].timestamp)
    self.assertEqual('b', self.cluster.events[0].kind)
    self.assertEqual('b', self.cluster.events[0].player)
    self.assertEqual(Point2(110, 98), self.cluster.events[0].point)
    self.assertEqual(19501, self.cluster.events[-1].timestamp)
    
  def test_blobs(self):
    self.assertEqual(30, len(self.cluster.blobs()))
    self.assertEqual(2562, self.cluster.blobs()[0].timestamp)
    self.assertEqual(12129, self.cluster.blobs()[-1].timestamp)
    
  def test_blobPoints(self):
    self.assertEqual(30, len(self.cluster.blobPoints()))
    self.assertEqual(Point2(110,98), self.cluster.blobPoints()[0])
    self.assertEqual(Point2(155,75), self.cluster.blobPoints()[-1])
  
  def test_verticalGridLine(self):
    vertical = PeekaboomRound(fixtures.verticalGridLine)
    self.assertEqual(3, len(vertical.blobs()))
    self.assertEqual(Point2(100., 0.), vertical.blobPoints()[0])
    self.assertEqual(Point2(100., 300.), vertical.blobPoints()[1])
    self.assertEqual(Point2(100., 200.), vertical.blobPoints()[2])
  
  def test_merge(self):
    vertical = PeekaboomRound(fixtures.verticalGridLine)
    merged = self.cluster.merge(vertical)
    self.assertEqual(37, len(self.cluster.events))
    self.assertEqual(3, len(vertical.events))
    self.assertEqual(40, len(merged.events))
    
  def test_threePoints(self):
    threePointRound = PeekaboomRound(fixtures.threePoints)
    self.assert_(threePointRound.cluster().widthAxis())
    self.assert_(threePointRound.cluster().lengthAxis())
    
    
    