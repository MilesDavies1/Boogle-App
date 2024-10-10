# Miles Davies @02921243
class Boggle:
    def __init__(self, grid=None, dictionary=None):
        self.grid = grid if grid is not None else []
        self.dictionary = set(dictionary) if dictionary is not None else set()
        self.solution = set()
        self.visited = {}

    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = set(dictionary)

    def getSolution(self):
        self.solution = set()
        
        if not self.grid or not self.dictionary:
            return list(self.solution)

        rows = len(self.grid)
        cols = len(self.grid[0])

        # Reset visited for each call
        self.visited = {}

        for r in range(rows):
            for c in range(cols):
                #zero out grid here
                self._dfs(r, c, "", self.dictionary)

        return list(self.solution)

    def _dfs(self, r, c, current_word, words_set):
        if (r, c) in self.visited:
            return

        current_word += self.grid[r][c]

        # Check if the current word is in the dictionary and has at least length 3
        if len(current_word) >= 3 and current_word in words_set:
            self.solution.add(current_word)

        # Mark the cell as visited
        self.visited[(r, c)] = True

        # Explore all 8 possible directions
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nr, nc = r + dr, c + dc
            if self._is_within_bounds(nr, nc) and (nr, nc) not in self.visited:
                self._dfs(nr, nc, current_word, words_set)

        # Backtrack by removing the cell from visited
        del self.visited[(r, c)]

    def _is_within_bounds(self, r, c):
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])

# Example usage
if __name__ == "__main__":
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

# class Boggle:
#     def __init__(self, grid, dictionary):
#         self.grid = grid
#         self.dictionary = dictionary
#         self.solutions = []

# def main():
#     grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
#     dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
#     mygame = Boggle(grid, dictionary)
#     print(mygame.getSolution())
