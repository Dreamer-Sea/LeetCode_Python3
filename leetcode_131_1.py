from typing import List


def is_palindrome(start: int, end: int, s: str) -> bool:
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s, 0, [], res)
        return res

    def backtracking(self,
                     s: str, start: int, temp: List[str], res: List[List[str]]):
        if start == len(s):
            res.append([i for i in temp])
            return
        for i in range(start, len(s)):
            if is_palindrome(start, i, s):
                self.backtracking(
                    s, i + 1, temp + [s[start:i + 1]], res)
            else:
                continue


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))


