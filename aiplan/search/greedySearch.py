from node import Node

class GreedySearch:

  def isGoal(self, node):
    if node.label == 'goal':
      return True

    return False

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

  def backtrack(self, node):
    path = []
    current = node
    path.append(node)

    while current.parent != None:
      current = current.parent
      path.insert(0, current)

    return path

  def printPath(self, path):
    str = "["
    for node in path:
      str += node.label + ","

    print(str + "]")

  def search(self, root, goal):
    node = root
    open = []

    self.expandNode(open, root)

    while len(open) > 0:
      node = self.best(open)
      open.remove(node)
      if self.isGoal(node):
        break
      self.expandNode(open, node)

    return self.backtrack(node)

