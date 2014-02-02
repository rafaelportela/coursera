from node import Node

class GreedySearch:

  def isGoal(self, node):
    if node.label == 'goal':
      return True

    return False

  def isNode(self, node):
    if isinstance(node, Node):
      return True

    return False

  def nextFrom(self, node):
    if len(node.links) > 0:
      return node.links[0]

    return None

  def expandNode(self, open, node):
    for child in node.links:
      open.append(child)

  def best(self, open):
    bestNode = open[0]

    if len(open) > 1:
      for i in range(1, len(open)):
        if open[i].data < bestNode.data:
          bestNode = open[i]

    return bestNode

  def printPath(self, path):
    str = "["
    for node in path:
      str += node.label + ","

    print(str + "]")

  def search(self, root, goal):
    path = []
    closed = []
    open = []

    path.append(root)
    self.expandNode(open, root)

    while len(open) > 0:

      node = self.best(open)
      open.remove(node)

      if self.isGoal(node):
        path.append(node)
        break

      path.append(node)
      self.expandNode(open, node)

    return path

