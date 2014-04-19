from node import Node
import unittest

class NodeHoldsLabelAndData(unittest.TestCase):

  def testNodeWithLabel(self):
    n = Node('label')
    self.assertEqual('label', n.label)

  def testNodeWithNoData(self):
    n = Node('label')
    self.assertEqual(None, n.data)

  def testNodeWithIntegerAsData(self):
    n = Node('label', 10)
    self.assertEqual(10, n.data)

  def testNodeWithStringAsData(self):
    n = Node('label', 'stuff')
    self.assertEqual('stuff', n.data)

class NodeIsLinkedToOtherNodes(unittest.TestCase):

  def testNodeWithLinkToOtherNode(self):
    n1 = Node('n1')
    n2 = Node('n2')
    n1.addLinkTo(n2)

    self.assertEqual('n2', n1.links[0].label)

  def testLinkWithParent(self):
    n1 = Node('n1')
    n2 = Node('n2')
    n1.addLinkTo(n2)

    self.assertEqual('n1', n2.parent.label)


class NodesAreComparedByLabel(unittest.TestCase):

  def testCompareByLabel(self):
    n1 = Node('a_node')
    n2 = Node('a_node')

    self.assertEqual(n1, n2)

  def testCompareWithNonNodeObj(self):
    n1 = Node('node')

    self.assertFalse(n1 == None)
