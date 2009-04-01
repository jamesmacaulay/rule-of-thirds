import unittest
import fixtures
from Photographer import *

class PhotographerTestCase(unittest.TestCase):
  
  def setUp(self):
    self.peekaboomRound = PeekaboomRound(fixtures.roundData)
    self.photographer = Photographer(self.peekaboomRound)
  
  def test_init(self):
    self.assertEqual(self.peekaboomRound, self.photographer.peekaboomRound)
  
  def test_relativize(self):
    self.assertEqual(0.5, self.photographer.relativize(1., 0., 2.))
    self.assertEqual(0.0, self.photographer.relativize(-1., 0., 2.))
    self.assertEqual(1.0, self.photographer.relativize(3., 0., 2.))
  
  def test_relativeRotationalAlignment(self):
    self.assert_(self.photographer.relativeRotationalAlignment(math.pi / 12.) >= 0.5)
  
  def test_relativeProximity(self):
    # relativeProximity goes up when you get closer
    self.assert_(self.photographer.relativeProximity(1./27.) > 0.5)
  
  def test_weightedAverage(self):
    self.assertEqual(6.0, self.photographer.weightedAverage(0.75, 3.0, 7.0))
  
  def test_rotationBetweenLines(self):
    p = self.photographer
    line = Photographer.gridlines[0]
    segment = LineSegment2(Point2(0., 0.), Vector2(1., 0.))
    r = p.rotationBetweenLines(line, segment)
    self.assertEqual(0.0, r)
  
  # def test_ruleOfThirds(self):
  #   print self.photographer.ruleOfThirds()
  
  def test_verticalGridLine(self):
    verticalRound = PeekaboomRound(fixtures.verticalGridLine)
    verticalPhotographer = Photographer(verticalRound)
    self.assertEqual(1.0, verticalPhotographer.clusterIsAlongLine(verticalPhotographer.gridlines[2]))
    self.assertEqual(1.0, verticalPhotographer.ruleOfThirds())