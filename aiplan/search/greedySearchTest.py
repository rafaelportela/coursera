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

  def testChoosingTheNextBestNode(self):
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

  def testNextBestOpenNodeWithBacktrack(self):
    root = Node('root')
    left = Node('left', 20)
    right = Node('right', 10)

    root.addLinkTo(left)
    root.addLinkTo(right)

    goal = Node('goal', 10)
    left.addLinkTo(goal)

    g = GreedySearch()
    path = g.search(root, goal)

    self.assertEqual([root, left, goal], path)

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

class BacktrackTest(unittest.TestCase):

  def testBacktracl(self):
    n1 = Node('n1')
    n2 = Node('n2')

    n1.addLinkTo(n2)

    path = GreedySearch().backtrack(n2)
    self.assertEqual([n1, n2], path)

if __name__ == '__main__':
  unittest.main()
