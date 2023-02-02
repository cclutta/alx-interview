#!/usr/bin/python3
import sys
""" N queens problem. """

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = []
    for i in range(n):
        board.append([i, None])

    def is_safe(x, y):
        """determines if position (x, y) is safe"""
        for z in range(n):
            if y == board[z][1]:
                return False

        i = 0
        while(i < x):
            if abs(board[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def solve(x):
        """solves and backtracks when encountering conflicts"""
        for y in range(n):
            for i in range(x, n):
                board[i][1] = None

            if is_safe(x, y):
                board[x][1] = y
                if (x == n - 1):
                    print(board)
                else:
                    solve(x + 1)

    solve(0)
