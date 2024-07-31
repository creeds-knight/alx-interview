#!/usr/bin/python3
"""
  The N Queens Problem
"""

import sys


class Solution:
    def nqueens(self, N: int):
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        res = []
        board = [["."] * N for _ in range(N)]

        def backtrack(r):
            if r == N:
                positions = [[row, board[row].index("Q")] for row in range(N)]
                res.append(positions)
                return

            for c in range(N):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Add the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # Move to the next row
                backtrack(r + 1)

                # Remove the queen
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    sol = Solution()
    solutions = sol.nqueens(N)
    for solution in solutions:
        print(solution)
