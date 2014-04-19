from node import Node
from greedyStrategy import GreedyStrategy
from bestFirstSearch import BestFirstSearch
import unittest

def bestFirstSearch():
    return BestFirstSearch( \
        GreedyStrategy(), \
        DefaultNodeExpander(), \
        CustomGoalVerifier())

class CustomGoalVerifier:

  def isGoal(self, data):
    if data == 0:
      return True

    return False

class DefaultNodeExpander:

  def expand(self, node):
    return node.links

class BestFirstSearchTest(unittest.TestCase):

  def testRootAsGoal(self):
    root = Node('goal', 0)
    g = bestFirstSearch()
    path = g.search(root, root)

    self.assertEqual([root], path)

  def testOnlyRootAndGoalNodes(self):
    root = Node('root', 10)
    goal = Node('goal', 0)
    root.addLinkTo(goal)

    g = bestFirstSearch()
    path = g.search(root, goal)

    self.assertEqual([root, goal], path)

  def testChoosingTheNextBestNode(self):
    root = Node('root')
    left = Node('left', 20)
    right = Node('right', 10)

    root.addLinkTo(left)
    root.addLinkTo(right)

    goal = Node('goal', 0)
    left.addLinkTo(goal)
    right.addLinkTo(goal)

    g = bestFirstSearch()
    path = g.search(root, goal)

    self.assertEqual([root, right, goal], path)

  def testNextBestOpenNodeWithBacktrack(self):
    root = Node('root')
    left = Node('left', 20)
    right = Node('right', 10)

    root.addLinkTo(left)
    root.addLinkTo(right)

    goal = Node('goal', 0)
    left.addLinkTo(goal)

    g = bestFirstSearch()
    path = g.search(root, goal)

    self.assertEqual([root, left, goal], path)


class CustomGoalVerifierTest(unittest.TestCase):

  def testGivenGoalComparator(self):
    root = Node('root', 10)
    goal = Node('the_goal', 0)
    other = Node('other', 20)

    root.addLinkTo(goal)
    goal.addLinkTo(other)

    g = bestFirstSearch()
    path = g.search(root, goal)

    self.assertEqual([root, goal], path)

from bestFirstSearch import Tracker

class BacktrackTest(unittest.TestCase):

  def testBacktracl(self):
    n1 = Node('n1')
    n2 = Node('n2')

    n1.addLinkTo(n2)

    path = Tracker().backtrack(n2)
    self.assertEqual([n1, n2], path)

if __name__ == '__main__':
  unittest.main()
