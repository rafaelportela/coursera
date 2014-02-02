from node import Node
from greedySearch import GreedySearch
import unittest

class GreedySearchTest(unittest.TestCase):

  def testRootAsGoal(self):
    root = Node('goal')
    g = GreedySearch()
    path = g.search(root, root)

    self.assertEqual([root], path)

  def testOnlyRootAndGoalNodes(self):
    root = Node('root')
    goal = Node('goal')
    root.addLinkTo(goal)

    g = GreedySearch()
    path = g.search(root, goal)

    self.assertEqual([root, goal], path)

  def testSmallBestPath(self):
    root = Node('root')
    left = Node('left', 20)
    right = Node('right', 10)

    root.addLinkTo(left)
    root.addLinkTo(right)

    goal = Node('goal', 10)
    left.addLinkTo(goal)
    right.addLinkTo(goal)

    g = GreedySearch()
    path = g.search(root, goal)

    self.assertEqual([root, right, goal], path)

class BestNodeSelectionTest(unittest.TestCase):

  def testSelectionFromOneElementArray(self):
    open = [Node('single', 10)]
    self.assertEqual(Node('single'), GreedySearch().best(open))

  def testBestIsFirstFromArray(self):
    open = [Node('not_best', 20), Node('best', 10)]
    self.assertEqual(Node('best'), GreedySearch().best(open))

  def testBestIsLastFromArray(self):
    open = [Node('best', 10), Node('other', 20)]
    self.assertEqual(Node('best'), GreedySearch().best(open))

if __name__ == '__main__':
  unittest.main()
