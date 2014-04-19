from node import Node
from closest_strategy import ClosestStrategy
import unittest

puzzle_goal = '012345678'
closest_puzzle = '102345678'
shuffle_puzzle = '087654321'

class ClosestStrategyTest(unittest.TestCase):

  def testSelectNextFromSingleNode(self):
    fringe = [Node('node')]
    s = ClosestStrategy(None)

    selected = s.selectNext(fringe)
    self.assertEqual(selected, fringe[0])

  def testSelectNoneFromEmptyFringe(self):
    fringe = []
    s = ClosestStrategy(None)

    selected = s.selectNext(fringe)
    self.assertEqual(selected, None)

class ClosestStrategyUseCustomComparator(unittest.TestCase):

  def testComparatorToCompareNodeData(self):
    n1 = Node('n1', CustomData('marcos'))
    n2 = Node('n2', CustomData('eduardo'))
    comparator = CustomDataComparator()

    fringe = [n1, n2]
    s = ClosestStrategy(comparator)

    selected = s.selectNext(fringe)
    self.assertEqual(selected, fringe[0])

class CustomData:

  def __init__(self, string):
    self.string = string

class CustomDataComparator:

  def compare(self, customdata1, customdata2):
    if len(customdata1.string) > len(customdata2.string):
      return 1
    elif len(customdata1.string) < len(customdata2.string):
      return -1
    else:
      return 0
