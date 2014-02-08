class Node:

  def __init__(self, label, data=None):
    self.label = label
    self.data = data
    self.links = []
    self.parent = None

  def addLinkTo(self, node):
    self.links.append(node)
    node.parent = self

  def __eq__(self, other):
    if not isinstance(other, Node):
      return False

    return self.label == other.label

