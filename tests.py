import unittest

from boggle_solver import Boggle


class TestBoggle(unittest.TestCase):

    def test_isValid_Grid(self):
        """
        Test that a valid grid returns True.
        """
        grid = [['A', 'B'], ['C', 'D']]
        self.assertTrue(Boggle.is_valid_grid(grid))

    def test_invalid_Grid_Empty(self):
        """
        Test that an empty grid returns False.
        """
        grid = []
        self.assertFalse(Boggle.is_valid_grid(grid))

    def test_invalid_Grid_Varying_Row_Lengths(self):
        """
        Test that grids with varying row lengths return False.
        """
        grid = [['A', 'B'], ['C']]
        self.assertFalse(Boggle.is_valid_grid(grid))

    def test_duplicate_letters(self):
        """
        Test that duplicate letters do not lead to immediate loops.
        """
        grid = [['A', 'A'], ['A', 'A']]
        dictionary = ['AA']
        game = Boggle(grid, dictionary)
        solution = game.getSolution()
        self.assertIn('AA', solution)

    def test_no_words_in_grid(self):
        """
        Test when no valid words can be formed.
        """
        grid = [['X', 'Y'], ['Z', 'Q']]
        dictionary = ['A', 'B', 'C']
        game = Boggle(grid, dictionary)
        solution = game.getSolution()
        self.assertEqual(solution, [])

    def test_words_cannot_end_with_S(self):
        """
        Test that words do not end with 'S'.
        """
        grid = [['A', 'B'], ['C', 'S']]
        dictionary = ['A', 'AB', 'AC', 'C']
        game = Boggle(grid, dictionary)
        solution = game.getSolution()
        self.assertNotIn('C', solution)

    def test_words_can_use_cell_once(self):
        """
        Test that a letter can only be used once in a word.
        """
        grid = [['A', 'B'], ['C', 'D']]
        dictionary = ['ABCD']
        game = Boggle(grid, dictionary)
        solution = game.getSolution()
        self.assertNotIn('ABCD', solution)

    def test_grid_case_1x1(self):
        """
        Test a 1x1 grid case.
        """
        grid = [['A']]
        dictionary = ['A']
        game = Boggle(grid, dictionary)
        solution = game.getSolution()
        self.assertIn('A', solution)

    def test_long_words(self):
        """
        Test that long words can be formed correctly.
        """
        grid = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        dictionary = ['ABCDEFG', 'ABCDEFGH']
        game = Boggle(grid, dictionary)
        solution = game.getSolution()
        self.assertIn('ABCDEFGH', solution)


if __name__ == "__main__":
    unittest.main()

