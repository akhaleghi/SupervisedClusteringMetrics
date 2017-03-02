"""
This class has a few unit tests for the ClusterMetrics class

Author: Abe Khaleghi
Email : amkhaleghi@gmail.com
"""
import unittest
from ClusterMetrics import *

class TestClusterMetrics(unittest.TestCase):
    def setUp(self):
        self.metrics = ClusterMetrics([0,0,0],[0,0,0])

class PurityTestCase(TestClusterMetrics):
    def runTest(self):
        assert self.metrics.rand_index() == 1.0

class RandIndexTestCase(TestClusterMetrics):
    def runTest(self):
        assert self.metrics.rand_index() == 1.0

class FMeasureTestCase(TestClusterMetrics):
    def runTest(self):
        assert self.metrics.rand_index() == 1.0

if __name__ == '__main__':
    unittest.main()