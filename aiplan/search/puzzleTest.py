import unittest
from puzzle import Puzzle

class PuzzleTest(unittest.TestCase):

  def testGoalStateHasNoDistance(self):
    p = Puzzle("012345678")
    self.assertEqual(p.distanceToGoal(), 0)

  def testHowManyMovesIsCurrentStateFromGoal(self):
    p = Puzzle("021345678")
    self.assertEqual(p.distanceToGoal(), 2)

from puzzle import Movement

class MovementTest(unittest.TestCase):

  def testHowManyMovesIsPieceFromCorrentPlace(self):
    m = Movement()
    piece_number = '8'
    current_position = 0
    moves = m.countMoves(piece_number, current_position)

    self.assertEqual(moves, 4)

from puzzle import PuzzleStateComparator

class PuzzleStateComparatorTest(unittest.TestCase):

  def testIfStateIsCloserToGoalThanOther(self):
    p1 = Puzzle("120345678")
    p2 = Puzzle("102345678")

    c = PuzzleStateComparator()
    result = c.compare(p1, p2)

    self.assertEqual(result, 1)

  def testDifferentStatesCanHaveSameDistanceToGoal(self):
    p1 = Puzzle("120345678")
    p2 = Puzzle("012345867")

    comparator = PuzzleStateComparator()
    result = comparator.compare(p1, p2)

    self.assertEqual(result, 0)

from puzzle import Generator

class GeneratorClass(unittest.TestCase):

  def testGeneratePossibleStatesFromCurrent(self):
    current = Puzzle("123456780")
    g = Generator()

    possibleStates = g.statesFrom(current)
    self.assertEqual(len(possibleStates), 2)

  def testIfStateCanMoveZeroUp(self):
    """ 123456780 has 0 in the last row, it can move up """
    zeroInLastRow = 8
    g = Generator()

    canMoveUp = g.canZeroMoveUp(zeroInLastRow)
    self.assertEqual(canMoveUp, True)

  def testIfStateCanMoveZeroDown(self):
    """ 123405678 has 0 in the center row, it can move down """
    zeroInCentreRow = 4
    g = Generator()

    canMoveDown = g.canZeroMoveDown(zeroInCentreRow)
    self.assertEqual(canMoveDown, True)

  def testIfStateCanMoveZeroRight(self):
    """ 012345678 has 0 at the left corner, it can move right"""
    zeroInLeftCorner = 0
    g = Generator()

    canMoveRight = g.canZeroMoveRight(zeroInLeftCorner)
    self.assertEqual(canMoveRight, True)

  def testIfStateCanMoveZeroLeft(self):
    """ 120345678 has 0 at the right corner, it can move left"""
    zeroInRightCorner = 2
    g = Generator()

    canMoveLeft = g.canZeroMoveLeft(zeroInRightCorner)
    self.assertEqual(canMoveLeft, True)

  def testMoveZeroUp(self):
    """ swap 0 and 2 """
    current  = "123405678"
    expected = "103425678"

    g = Generator()
    state = g.moveZeroUp(current)
    self.assertEqual(state, expected)

  def testMoveZeroDown(self):
    """ swap 0 and 8 """
    current  = "123450678"
    expected = "123458670"

    g = Generator()
    state = g.moveZeroDown(current)
    self.assertEqual(state, expected)

  def testMoveZeroRight(self):
    current  = "012345678"
    expected = "102345678"

    state = Generator().moveZeroRight(current)
    self.assertEqual(state, expected)

  def testMoveZeroLeft(self):
    current  = "123450678"
    expected = "123405678"

    state = Generator().moveZeroLeft(current)
    self.assertEqual(state, expected)

from puzzle import GoalVerifier

class GoalVerifierTest(unittest.TestCase):

  def testIfNodeIsGoalNode(self):
    puzzle = Puzzle("012345678")

    verifier = GoalVerifier()
    self.assertTrue(verifier.isGoal(puzzle))

if __name__ == '__main__':
  unittest.main()
