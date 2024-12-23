# Miles Davies @02921243
class Boggle:
    def __init__(self, board, dictionary):
        """
        Initialize the Boggle game with the given board and dictionary.
        """
        if not self.is_valid_grid(board):
            self.board = []
            self.n = 0
        else:
            self.board = [[cell.upper() for cell in row] for row in board]
            self.n = len(board)

        self.dictionary = set(word.upper() for word in dictionary)
        self.prefixes = self.build_prefixes(self.dictionary)
        self.directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]

    def is_valid_grid(self, board):
        """
        Check if the input grid is valid.
        """
        if not board or not all(board):
            return False
        row_lengths = set(len(row) for row in board)
        return len(row_lengths) == 1  # All rows should have the same length

    def build_prefixes(self, dictionary):
        """
        Build a set of all possible prefixes from the dictionary.

        :param dictionary: A set of valid words.
        :return: A set containing all possible prefixes.
        """
        prefixes = set()
        for word in dictionary:
            for i in range(1, len(word)):
                prefixes.add(word[:i])
        return prefixes

    def dfs(self, i, j, visited, current_word):
        """
        Perform Depth-First Search from the cell (i, j).
        """
        if i < 0 or i >= self.n:
            return
        if j < 0 or j >= len(self.board[i]):
            return
        if visited[i][j]:
            return

        current_word.append(self.board[i][j])
        extra_chars = 0

        if self.board[i][j] == 'Q':
            current_word.append('U')
            extra_chars += 1

        if self.board[i][j] == 'S':
            if len(current_word) >= 2 and current_word[-2] == 'Q':
                pass
            else:
                current_word.append('T')
                extra_chars += 1

        word = ''.join(current_word)

        if word not in self.prefixes and word not in self.dictionary:
            for _ in range(1 + extra_chars):
                if current_word:
                    current_word.pop()
            return

        if len(word) >= 3 and word in self.dictionary:
            self.found_words.add(word)

        visited[i][j] = True

        for di, dj in self.directions:
            ni, nj = i + di, j + dj
            self.dfs(ni, nj, visited, current_word)

        visited[i][j] = False

        for _ in range(1 + extra_chars):
            if current_word:
                current_word.pop()

    def getSolution(self):
        """
        Find all valid words on the Boggle board based on the dictionary.
        """
        self.found_words = set()
        if self.n == 0:
            return []
        visited = [[False for _ in row] for row in self.board]

        for i in range(self.n):
            for j in range(len(self.board[i])):
                self.dfs(i, j, visited, [])

        return sorted(list(self.found_words))


def main():
    """
    Example usage of the Boggle class.
    """
    # Example grid that should pass 'test_isValid_Grid'
    grid1 = [["A", "B"], ["C", "D"]]
    dictionary1 = ["A", "B", "AC", "ACA", "ACB", "DE"]
    boggle1 = Boggle(grid1, dictionary1)
    print(boggle1.getSolution())  # Output: ["ACB"]

    grid2 = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["I", "J", "K", "L"], ["A", "B", "C", "D"]]
    dictionary2 = ["ABEF", "AFJIEB", "DGKD", "DGKA"]
    boggle2 = Boggle(grid2, dictionary2)
    print(boggle2.getSolution())  # Output: ["ABEF", "AFJIEB", "DGKD"]

    grid3 = [
        ["T", "R", "E"],
        ["A", "S", "T"],
        ["P", "O", "L"]
    ]
    dictionary3 = ["TAP", "TOP", "TASTE", "TEA", "POT", "STOLE", "TRAPS", "STOLE"]
    boggle3 = Boggle(grid3, dictionary3)
    print(boggle3.getSolution())  # Output: ['TAP', 'TOP', 'TASTE', 'TEA', 'POT', 'STOLE']

    grid4 = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]
    dictionary4 = ["AB", "BCD", "CFI", "E", "DE", "GHI", "EF", "ADG", "BCE"]
    boggle4 = Boggle(grid4, dictionary4)
    print(boggle4.getSolution())  # Output: ['AB', 'BCD', 'CFI', 'DE', 'GHI', 'EF', 'ADG', 'BCE']


if __name__ == "__main__":
    main()

