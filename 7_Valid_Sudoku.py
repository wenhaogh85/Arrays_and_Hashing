"""
Valid Sudoku (Medium)

Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
                [["5","3",".", ".","7",".", ".",".","."]
                ,["6",".",".", "1","9","5", ".",".","."]
                ,[".","9","8", ".",".",".", ".","6","."]
                ,["8",".",".", ".","6",".", ".",".","3"]
                ,["4",".",".", "8",".","3", ".",".","1"]
                ,["7",".",".", ".","2",".", ".",".","6"]
                ,[".","6",".", ".",".",".", "2","8","."]
                ,[".",".",".", "4","1","9", ".",".","5"]
                ,[".",".",".", ".","8",".", ".","7","9"]]
Output: true

Example 2:
Input: board =
                [["8","3",".", ".","7",".", ".",".","."]
                ,["6",".",".", "1","9","5", ".",".","."]
                ,[".","9","8", ".",".",".", ".","6","."]
                ,["8",".",".", ".","6",".", ".",".","3"]
                ,["4",".",".", "8",".","3", ".",".","1"]
                ,["7",".",".", ".","2",".", ".",".","6"]
                ,[".","6",".", ".",".",".", "2","8","."]
                ,[".",".",".", "4","1","9", ".",".","5"]
                ,[".",".",".", ".","8",".", ".","7","9"]]
Output: false
Explanation: Same as Example 1,
except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

# ------------------------------------
# dataset

board = [["5","3",".", ".","7",".", ".",".","."]
        ,["6",".",".", "1","9","5", ".",".","."]
        ,[".","9","8", ".",".",".", ".","6","."]
        ,["8",".",".", ".","6",".", ".",".","3"]
        ,["4",".",".", "8",".","3", ".",".","1"]
        ,["7",".",".", ".","2",".", ".",".","6"]
        ,[".","6",".", ".",".",".", "2","8","."]
        ,[".",".",".", "4","1","9", ".",".","5"]
        ,[".",".",".", ".","8",".", ".","7","9"]]

board_2 =   [["8","3",".", ".","7",".", ".",".","."]
            ,["6",".",".", "1","9","5", ".",".","."]
            ,[".","9","8", ".",".",".", ".","6","."]
            ,["8",".",".", ".","6",".", ".",".","3"]
            ,["4",".",".", "8",".","3", ".",".","1"]
            ,["7",".",".", ".","2",".", ".",".","6"]
            ,[".","6",".", ".",".",".", "2","8","."]
            ,[".",".",".", "4","1","9", ".",".","5"]
            ,[".",".",".", ".","8",".", ".","7","9"]]

# ------------------------------------
# my solution
# time: ? | space: ?
def mySolution(board):

    # checks each row for duplicate digits
    for row in board:

        digits = []

        for digit in row:

            if digit in digits:
                return False

            elif digit != ".":
                    digits.append(digit)

    # checks each column for duplicate digits
    for column in range(len(board[0])):

        digits = []

        for row in range(len(board)):

            digit = board[row][column]

            if digit in digits:
                return False

            elif digit != ".":
                digits.append(digit)

    # checks each 3 x 3 sub-boxes for duplicate digits
    # (use Excel diagram to visualise iteration)

    # initialises boundaries
    start_column = 0
    end_column = 3
    start_row = 0
    end_row = 3
    for iteration in range(len(board)):

        # adjusts boundaries for 4th and 7th 3 x 3 sub-boxes
        if iteration > 0 and iteration % 3 == 0:
            start_column = 0
            end_column = 3
            start_row += 3
            end_row += 3

        # print(
        #     "\n==========================" +
        #     "\ncolumns range: {} - {}".format(start_column, end_column) +
        #     "\nrows range   : {} - {}\n".format(start_row, end_row) +
        #     "\nsub-box:"
        # )

        # loops through 3 x 3 sub-box based on defined boundaries
        for row in range(start_row, end_row):

            digits = []

            for column in range(start_column, end_column):

                digit = board[row][column]

                # print(digit, end=" ")

                if digit in digits:
                    return False

                elif digit != ".":
                    digits.append(digit)

            # print()

        # adjusts boundaries to iterate next sub-box
        start_column += 3
        end_column += 3

    # print()

    # returns True if it passes all duplicate checks
    return True

print(mySolution(board))

# ------------------------------------
# optimal solution
# time: O(9^2) | space: O(9^2)
from collections import defaultdict

def solution(board):

    columns = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set) # key = (row/3, column/3) integer division

    for row in range(9):
        for column in range(9):

            # print(
            #     "\n==================" +
            #     "\ncolumns: {}".format(dict(columns)) +
            #     "\nrows   : {}".format(dict(rows)) +
            #     "\nsquares: {}".format(dict(squares)) +
            #     "\n\ndigit  : {}".format(board[row][column])
            # )

            digit = board[row][column]

            if digit == ".":
                continue

            if (digit in rows[row] or
                digit in columns[column] or
                digit in squares[(row // 3, column // 3)]):
                return False

            columns[column].add(digit)
            rows[row].add(digit)
            squares[(row // 3, column // 3)].add(digit)

    return True

print(solution(board))