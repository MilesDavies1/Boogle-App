#miles davies @02921243
import unittest
import sys

sys.path.append("/home/codio/workspace/")  # Path to find boggle_solver.py and Boggle Class

from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

  # Test for a 3x3 grid
  def test_Normal_case_3x3(self):
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["abc", "abdhi"]
    expected = [x.upper() for x in expected]
    self.assertEqual(sorted(expected), sorted(solution))

  # Test for 4x4 grid
  def test_Scalability_case_4x4(self):
    grid = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["I", "J", "K", "L"], ["M", "N", "O", "P"]]
    dictionary = ["abcd", "efgh", "ijkl", "mnop", "aeim", "dgpl"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["abcd", "efgh", "ijkl", "mnop", "aeim", "dgpl"]
    expected = [x.upper() for x in expected]
    self.assertEqual(sorted(expected), sorted(solution))

  # Test for 5x5 grid
  def test_Scalability_case_5x5(self):
    grid = [["A", "B", "C", "D", "E"], ["F", "G", "H", "I", "J"], ["K", "L", "M", "N", "O"],
            ["P", "Q", "R", "S", "T"], ["U", "V", "W", "X", "Y"]]
    dictionary = ["abcde", "fghij", "klmno", "pqrst", "uvwxyz", "aeimq", "dglpx"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["abcde", "fghij", "klmno", "pqrst", "aeimq", "dglpx"]
    expected = [x.upper() for x in expected]
    self.assertEqual(sorted(expected), sorted(solution))

  # Additional scalability tests for larger grids (6x6, 7x7, 13x13, etc.) can follow the same pattern.

class TestSuite_Simple_Edge_Cases(unittest.TestCase):

  # Test case for a 1x1 grid
  def test_SquareGrid_case_1x1(self):
    grid = [["A"]]
    dictionary = ["a", "b", "c"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    self.assertEqual(sorted(expected), sorted(solution))

  # Test case for an empty grid
  def test_EmptyGrid_case_0x0(self):
    grid = [[]]
    dictionary = ["hello", "there", "general", "kenobi"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    self.assertEqual(sorted(expected), sorted(solution))

  # Test case for a non-square grid (2x3)
  def test_NonSquareGrid_case_2x3(self):
    grid = [["A", "B", "C"], ["D", "E", "F"]]
    dictionary = ["abc", "def", "ab", "cf"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["ABC", "DEF", "AB", "CF"]
    expected = [x.upper() for x in expected]
    self.assertEqual(sorted(expected), sorted(solution))

class TestSuite_Complete_Coverage(unittest.TestCase):

  # Complex test case for complete coverage of dictionary and grid interactions
  def test_Complex_Case(self):
    grid = [["Q", "U", "I", "C", "K"], ["B", "R", "O", "W", "N"], ["F", "O", "X", "J", "U"], ["M", "P", "S", "A", "Z"], ["Y", "D", "T", "H", "E"]]
    dictionary = ["quick", "brown", "fox", "jump", "jumps", "over", "lazy", "dog"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["QUICK", "BROWN", "FOX", "JUMP", "JUMPS", "DOG"]
    expected = [x.upper() for x in expected]
    self.assertEqual(sorted(expected), sorted(solution))

class TestSuite_Qu_and_St(unittest.TestCase):

  # Test case to handle 'QU' pattern in the grid
  def test_Qu_Pattern(self):
    grid = [["Q", "U", "I", "C"], ["K", "L", "M", "N"], ["O", "P", "Q", "U"], ["R", "S", "T", "U"]]
    dictionary = ["quick", "quit", "quip", "quota"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["QUICK", "QUIT", "QUIP", "QUOTA"]
    expected = [x.upper() for x in expected]
    self.assertEqual(sorted(expected), sorted(solution))

  # Test case for 'ST' pattern
  def test_St_Pattern(self):
    grid = [["S", "T", "U", "V"], ["W", "X", "Y", "Z"], ["A", "B", "C", "D"], ["E", "F", "G", "H"]]
    dictionary = ["start", "stun", "stop", "stem"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["START", "STUN", "STOP", "STEM"]
    expected = [x.upper() for x in expected]
    self.assertEqual(sorted(expected), sorted(solution))

if __name__ == '__main__':
  unittest.main()
