from typing import List


def is_valid(s: str, start: int, end: int, dp: List[List[int]]) -> bool:
    if end - start + 1 > 1 and s[start] == "0":
        dp[start][end] = 2
        return False
    num = int(s[start:end+1])
    if num > 255:
        dp[start][end] = 2
        return False
    dp[start][end] = 1
    return True


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = list()
        dp = [list() for _ in range(len(s))]
        for i in range(len(s)):
            dp[i] = [0 for _ in range(len(s))]
        self.backtracking(s, 0, [], res, dp)
        return res

    def backtracking(self,
                     s: str, start: int, temp: List[str],
                     res: List[str], dp: List[List[int]]):
        if len(temp) == 4 and start == len(s):
            res.append(".".join(temp))
            return
        for i in range(start, len(s)):
            if dp[start][i] == 1 or (dp[start][i] == 0 and is_valid(s, start, i, dp)):
                self.backtracking(s, i+1, temp + [s[start:i+1]], res, dp)
            else:
                return


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
