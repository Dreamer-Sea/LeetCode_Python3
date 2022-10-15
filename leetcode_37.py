from typing import List


def is_valid(row: int, col: int, val: str, board: List[List[str]]) -> bool:
    for i in range(9):
        if board[i][col] == val:
            return False

    for j in range(9):
        if board[row][j] == val:
            return False

    start_row = int((row / 3)) * 3
    start_col = int((col / 3)) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == val:
                return False

    return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtracking() -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        continue
                    for k in range(1, 10):
                        val = str(int("0") + k)
                        if not is_valid(i, j, val, board):
                            continue
                        board[i][j] = val
                        if backtracking():
                            return True
                        board[i][j] = "."
                    return False
            return True

        backtracking()


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    s.solveSudoku(board=board)
    print(board)
