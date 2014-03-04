class Puzzle:

  def __init__(self, state):
    self.state = state

  def distanceToGoal(self):
    m = Movement()
    moves = 0

    for i in range(0, 9):
      moves += m.countMoves(self.state[i], i)

    return moves

class Movement:

  def countMoves(self, piece, position):
    num = int(piece)

    targetVPos = num % 3
    targetHPos = int(num / 3) 

    currentVPos = position % 3
    currentHPos = int(position / 3)

    vMoves = abs(targetVPos - currentVPos) 
    hMoves = abs(targetHPos - currentHPos) 

    return vMoves + hMoves

class PuzzleStateComparator:

  def compare(self, aPuzzle, otherPuzzle):
    d1 = aPuzzle.distanceToGoal()
    d2 = otherPuzzle.distanceToGoal()

    if d1 > d2:
      return 1
    elif d1 < d2:
      return -1
    else:
      return 0

class Generator:

  def statesFrom(self, current):
    zeroIndex = current.state.rfind('0')
    possibleStates = []

    if self.canZeroMoveUp(zeroIndex):
      possibleStates.append(self.moveZeroUp(current.state))

    if self.canZeroMoveDown(zeroIndex):
      possibleStates.append(self.moveZeroDown(current.state))

    if self.canZeroMoveRight(zeroIndex):
      possibleStates.append(self.moveZeroRight(current.state))

    if self.canZeroMoveLeft(zeroIndex):
      possibleStates.append(self.moveZeroLeft(current.state))

    return possibleStates

  def canZeroMoveUp(self, zeroIndex):
    if self.row(zeroIndex) > 0:
      return True
    else:
      return False

  def canZeroMoveDown(self, zeroIndex):
    if self.row(zeroIndex) < 2:
      return True
    else:
      return False

  def canZeroMoveRight(self, zeroIndex):
    if self.column(zeroIndex) < 2:
      return True
    else:
      return False

  def canZeroMoveLeft(self, zeroIndex):
    if self.column(zeroIndex) > 0:
      return True
    else:
      return False

  def moveZeroUp(self, state):
    index = state.rfind('0')
    target = index - 3

    return \
        state[0:target] + \
        state[index] + \
        state[target+1:index] + \
        state[target] + \
        state[index+1::]

  def moveZeroDown(self, state):
    index = state.rfind('0')
    target = index + 3

    return \
        state[0:index] + \
        state[target] + \
        state[index+1:target] + \
        state[index] + \
        state[target+1::]
  
  def moveZeroRight(self, state):
    index = state.rfind('0')
    target = index + 1

    return \
        state[0:index] + \
        state[target] + \
        state[index+1:target] + \
        state[index] + \
        state[target+1::]

  def moveZeroLeft(self, state):
    index = state.rfind('0')
    target = index - 1

    return \
        state[0:target] + \
        state[index] + \
        state[target+1:index] + \
        state[target] + \
        state[index+1::]

  def row(self, index):
    return int(index / 3)

  def column(self, index):
    return int(index % 3)

class GoalVerifier:

  def isGoal(self, puzzle):
    if puzzle.state == '012345678':
      return True
    else:
      return False

