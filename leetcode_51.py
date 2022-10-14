from typing import List


def is_no_attack(row: int, col: int, board: List[List[str]]) -> bool:
    for i in range(len(board)):
        if board[i][col] == "Q":
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [list() for _ in range(n)]

        for i in range(n):
            board[i] = ["." for _ in range(n)]

        res = []

        def backtracking(row: int):
            if row == n:
                temp = ["".join(r) for r in board]
                res.append(temp)
                return
            for j in range(n):
                if board[row][j] != ".":
                    continue
                if not is_no_attack(row, j, board):
                    continue
                board[row][j] = "Q"
                backtracking(row + 1)
                board[row][j] = "."

        backtracking(0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
