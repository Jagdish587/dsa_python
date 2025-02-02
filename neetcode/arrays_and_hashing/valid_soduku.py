# https://neetcode.io/problems/valid-sudoku

from collections import defaultdict

# Initialize a defaultdict where each key maps to a set
squares = defaultdict(set)

# Example values for board positions
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Iterating over the board to fill the squares dictionary
for r in range(9):
    for c in range(9):
        num = board[r][c]
        if num != 0:  # Ignore empty cells
            key = (r // 3, c // 3)  # Determine the 3×3 sub-grid index
            squares[key].add(num)  # Add the number to the corresponding set

# Print squares dictionary
for key, values in squares.items():
    print(f"Sub-grid {key}: {values}")

print("final\n")
print(squares)



from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True   
        