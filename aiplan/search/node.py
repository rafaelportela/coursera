class Node:

  def __init__(self, label, data=None):
    self.label = label
    self.data = data
    self.links = []

  def addLinkTo(self, node):
    self.links.append(node)

  def __eq__(self, other):
    return self.label == other.label

