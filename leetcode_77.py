from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(n, k, 1, res, [])
        return res

    def backtracking(self, n, k, start: int, res: List[List[int]], temp: List[int]):
        if len(temp) == k:
            res.append([i for i in temp])
            return
        if start > n - (k - len(temp)) + 1:
            return
        for i in range(start, n+1):
            self.backtracking(n, k, i+1, res, temp+[i])


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
