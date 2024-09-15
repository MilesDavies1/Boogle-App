#Miles Davies @02921243

class Boggle:
    def __init__(self, grid=None, dictionary=None):
        # Initialize the Boggle solver with an optional grid and dictionary
        self.grid = grid if grid is not None else []
        self.dictionary = set(dictionary) if dictionary is not None else set()
        self.solution = set()  # To store found valid words
        self.visited = []  # To track visited tiles in the grid
        
    def setGrid(self, grid):
        # Set or update the grid
        self.grid = grid
        
    def setDictionary(self, dictionary):
        # Set or update the dictionary (convert list to set for fast lookups)
        self.dictionary = set(dictionary)
        
    def getSolution(self):
        # Find and return all valid words found in the grid
        self.solution = set()
        
        # If grid or dictionary is not set, return an empty list
        if not self.grid or not self.dictionary:
            return list(self.solution)
        
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        # Initialize the visited matrix to keep track of visited tiles
        self.visited = [[False] * cols for _ in range(rows)]
        
        # Start DFS from each tile in the grid
        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, "", self.dictionary)
        
        return list(self.solution)
    
    def _dfs(self, r, c, current_word, words_set):
        # Check if the current tile is already visited
        if self.visited[r][c]:
            return
        
        # Add the current tile's letter to the current word
        current_word += self.grid[r][c]
        
        # If the current word is valid and in the dictionary, add it to the solution
        if len(current_word) >= 3 and current_word in words_set:
            self.solution.add(current_word)
        
        # Mark the current tile as visited
        self.visited[r][c] = True
        
        # Explore all 8 possible directions (including diagonals)
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nr, nc = r + dr, c + dc  # Calculate the new row and column
            if self._is_within_bounds(nr, nc):
                self._dfs(nr, nc, current_word, words_set)
        
        # Unmark the current tile as visited (backtrack)
        self.visited[r][c] = False
    
    def _is_valid(self, r, c):
        # Check if the coordinates are within the grid bounds
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])
    
    def _is_within_bounds(self, r, c):
        # Check if the coordinates are within the grid bounds
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
