from typing import List


def is_valid(s: str, start: int, end: int) -> bool:
    if end - start + 1 > 1 and s[start] == "0":
        return False
    num = int(s[start:end+1])
    if num > 255:
        return False
    return True


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        dp = [list() for _ in range(len(s))]
        for i in range(len(s)):
            dp[i] = [False for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if is_valid(s, j, i):
                    dp[j][i] = True
        self.backtracking(s, 0, [], res, dp)
        return res

    def backtracking(self,
                     s: str, start: int, temp: List[str],
                     res: List[str], dp: List[List[bool]]):
        if len(temp) == 4 and start == len(s):
            res.append(".".join(temp))
            return

        for i in range(start, len(s)):
            if dp[start][i]:
                self.backtracking(s, i+1, temp + [s[start:i+1]], res, dp)
            else:
                return


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
