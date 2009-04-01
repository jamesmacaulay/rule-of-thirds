import unittest
from PointCluster import *

class PointClusterTestCase(unittest.TestCase):
  
  def setUp(self):
    self.points = [Point2(0.,0.), Point2(0.,10.), Point2(2., 1.), Point2(-2., 2.), Point2(0., 4.)]
    self.cluster = PointCluster(self.points)
  
  def test_lengthAxis(self):
    self.assertEqual(self.points[0], self.cluster.lengthAxis().p1)
    self.assertEqual(self.points[1], self.cluster.lengthAxis().p2)
  
  def test_widthAxis(self):
    self.assertEqual(Point2(-2., 1.5), self.cluster.widthAxis().p1)
    self.assertEqual(Point2(2., 1.5), self.cluster.widthAxis().p2)
  
  def test_centre(self):
    self.assertEqual(Point2(0.00, 3.40), self.cluster.centre())
    
    c = PointCluster([Point2(0.,0.), Point2(2., 2.)])
    self.assertEqual(Point2(1., 1.), c.centre())
  
  def test_twoPoints(self):
    twoPointCluster = PointCluster(self.points[0:2])
    self.assertEqual(10, twoPointCluster.lengthAxis().length)