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

if __name__ == '__main__':
  unittest.main()

