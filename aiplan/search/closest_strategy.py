class ClosestStrategy:

  def __init__(self, dataComparator):
    self.comparator = dataComparator

  def selectNext(self, fringe):

    if len(fringe) == 0:
      return None

    lowest = fringe[0].data
    selected = 0

    for i in range(1, len(fringe)):
      if self.comparator.compare(fringe[i].data, lowest) < 1:
        lowest = fringe[i].data
        selected = i

    return fringe[selected]
