#!/usr/bin/env python
import unittest

from tests.PeekaboomRoundTestCase import *
from tests.PeekaboomEventTestCase import *
from tests.PointClusterTestCase import *
from tests.PhotographerTestCase import *

suite = unittest.makeSuite(PeekaboomRoundTestCase, 'test')
suite.addTest(unittest.makeSuite(PeekaboomEventTestCase, 'test'))
suite.addTest(unittest.makeSuite(PointClusterTestCase, 'test'))
suite.addTest(unittest.makeSuite(PhotographerTestCase, 'test'))

runner = unittest.TextTestRunner()
runner.run(suite)

