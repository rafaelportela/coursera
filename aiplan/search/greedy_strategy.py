class GreedyStrategy:

  def selectNext(self, fringe):

    if len(fringe) == 0:
      return None

    lowest = fringe[0].data
    selected = 0

    for i in range(1, len(fringe)):
      if fringe[i].data < lowest:
        lowest = fringe[i].data
        selected = i

    return fringe[selected]
