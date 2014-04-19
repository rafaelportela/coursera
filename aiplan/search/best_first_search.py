from node import Node


class Tracker:

  def backtrack(self, node):
    path = []
    current = node
    path.append(node)

    while current.parent != None:
      current = current.parent
      path.insert(0, current)

    return path

class BestFirstSearch:

  def __init__(self, strategy, expander, goalVerifier):
    self.strategy = strategy
    self.expander = expander
    self.goalVerifier = goalVerifier

  def expandNode(self, open, visited, node):
    new_nodes = self.expander.expand(node)
    for new in new_nodes:
      if new not in visited:
        open.append(new)

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
    node = root
    open = []
    visited = []

    self.expandNode(open, visited, root)

    while len(open) > 0:
      node = self.strategy.selectNext(open)
      visited.append(node)

      open.remove(node)
      if self.goalVerifier.isGoal(node.data):
        break
      self.expandNode(open, visited, node)

    return Tracker().backtrack(node)

