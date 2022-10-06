from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = list()
        dp = list()
        for i in range(len(s)):
            dp.append(list())
            for j in range(len(s)):
                dp[i].append(False)
        for i in range(len(s)):
            for j in range(0, i+1):
                if s[i] == s[j] and (i-j < 2 or dp[j+1][i-1]):
                    dp[j][i] = True
        self.backtracking(s, 0, [], res, dp)
        return res

    def backtracking(self,
                     s: str, start: int, temp: List[str],
                     res: List[List[str]], dp: List[List[bool]]):
        if start == len(s):
            res.append([i for i in temp])
            return
        for i in range(start, len(s)):
            if not dp[start][i]:
                continue
            self.backtracking(s, i+1, temp+[s[start:i+1]], res, dp)


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
