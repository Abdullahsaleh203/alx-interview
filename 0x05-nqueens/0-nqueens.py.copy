#!/usr/bin/python3
""""""
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

N = sys.argv[1]
if N is not isinstance(N, int):
    print('N must be a number')
    sys.exit(1)

if int(N) < 4:
    print('N must be at least 4')
    sys.exit(1)


# A helper function to check if a queen can be placed in a given position
def is_safe(board, row, column):
    """A function to check if a queen can be placed in a given position"""
    N = len(board)
    # Check if there is already a queen in the same column
    for i in range(N):
        if [i][column] == 'Q':
            return False
        # Check if there is already a queen in the same row
        if [i][row] == 'Q':
            return False
        # Check if there is already a queen in the same upper diagonal
        for i, j in enumerate(range(row, -1, -1)):
            if board[i][j] == 'Q':
                return False
        # Check if there is already a queen in the same lower diagonal
        for i, j in enumerate(range(row, N, 1)):
            if board[i][j] == 'Q':
                return False
        return True


def nqueens(board, row):
    """Solve the nqueens"""
    n = len(board)
    if row == n:
        print(' '.join(board[i]) for i in range(n))
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            nqueens(board, row + 1)
            board[row][col] = "."


board = [["."] * N for _ in range(N)]
nqueens(board, 0)
