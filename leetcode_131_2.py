from typing import List


def is_palindrome_2(start: int, end: int, s: str, dp: List[List[int]]) -> bool:
    left, right = start, end
    while left < right:
        if s[left] != s[right]:
            dp[left][right] = 2
            return False
        left += 1
        right -= 1
    dp[start][end] = 1
    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        dp = [list() for i in range(len(s))]
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                dp[i].append(0)
        self.backtracking(s, 0, [], res, dp)
        return res

    def backtracking(self,
                     s: str, start: int, temp: List[str],
                     res: List[List[str]], dp: List[List[int]]):
        if start == len(s):
            res.append([i for i in temp])
            return
        for i in range(start, len(s)):
            if dp[start][i] == 1 or (dp[start][i] == 0 and is_palindrome_2(start, i, s, dp)):
                self.backtracking(s, i+1, temp+[s[start: i+1]], res, dp)
            else:
                continue


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
