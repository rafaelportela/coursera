from node import Node
from greedy_strategy import GreedyStrategy
import unittest

class GreedyStrategyTest(unittest.TestCase):

  def testSelectNextFromSingleNode(self):
    fringe = [Node('node')]
    g = GreedyStrategy()

    node = g.selectNext(fringe)
    self.assertEqual(node, fringe[0])

  def testSelectNextWithLowestValue(self):
    fringe = [Node('n1', 10), Node('n2', 5), Node('n3', 15)]
    g = GreedyStrategy()

    selected = g.selectNext(fringe)
    self.assertEqual(selected.label, fringe[1].label)

  def testSelectNoneWhenEmptyFringe(self):
    fringe = []
    g = GreedyStrategy()

    selected = g.selectNext(fringe)
    self.assertEqual(selected, None)
