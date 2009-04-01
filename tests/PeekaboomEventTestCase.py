import unittest
from PeekaboomEvent import *

class PeekaboomEventTestCase(unittest.TestCase):
  
  def setUp(self):
    self.boom_blob  = PeekaboomEvent([["2562", "b"],  [["b"], ["110", "98"]]])
    self.peek_guess = PeekaboomEvent([["8803", "p"],  [["g"], ["shark"]]])
    self.blob_hint  = PeekaboomEvent([["12356", "b"], [["h"], ["n"]]])
    self.peek_pass  = PeekaboomEvent([["19501", "p"], [["x"], []]])
  
  def test_init(self):
    self.assertEqual(2562, self.boom_blob.timestamp)
    self.assertEqual('b', self.boom_blob.player)
    self.assertEqual('b', self.boom_blob.kind)
    self.assertEqual(Point2(110, 98), self.boom_blob.point)
    self.assertEqual(None, self.boom_blob.guess)
    self.assertEqual(None, self.boom_blob.hint)
    
    self.assertEqual(8803, self.peek_guess.timestamp)
    self.assertEqual('p', self.peek_guess.player)
    self.assertEqual('g', self.peek_guess.kind)
    self.assertEqual(None, self.peek_guess.point)
    self.assertEqual('shark', self.peek_guess.guess)
    self.assertEqual(None, self.peek_guess.hint)
    
    self.assertEqual(12356, self.blob_hint.timestamp)
    self.assertEqual('b', self.blob_hint.player)
    self.assertEqual('h', self.blob_hint.kind)
    self.assertEqual(None, self.blob_hint.point)
    self.assertEqual(None, self.blob_hint.guess)
    self.assertEqual('n', self.blob_hint.hint)
    
    self.assertEqual(19501, self.peek_pass.timestamp)
    self.assertEqual('p', self.peek_pass.player)
    self.assertEqual('x', self.peek_pass.kind)
    self.assertEqual(None, self.peek_pass.point)
    self.assertEqual(None, self.peek_pass.guess)
    self.assertEqual(None, self.peek_pass.hint)