#!/usr/bin/python3
import sys


def nqueens(n: int):
    """
    backtracking
    """
    def backtrack(row, queens, diagonals, anti_diagonals, board):
        if row == n:
            # found a valid solution
            print([[i, j] for i, j in queens])
            return

        for col in range(n):
            # check if it is safe to place a queen in this position
            if col not in board and row - \
                    col not in diagonals and row + col not in anti_diagonals:
                board.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                queens.append((row, col))

                backtrack(row + 1, queens, diagonals, anti_diagonals, board)

                board.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
                queens.pop()

    board = set()
    queens = []
    diagonals = set()
    anti_diagonals = set()

    backtrack(0, queens, diagonals, anti_diagonals, board)

    if not queens:
        print("No solution found for {}-queens.".format(n))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)

    nqueens(n)
