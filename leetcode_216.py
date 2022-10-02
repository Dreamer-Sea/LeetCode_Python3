from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtracking(k, n, res, 1, 0, [])
        return res

    def backtracking(
            self,
            k: int, n: int, res: List[List[int]],
            start: int, tmp_sum: int, temp: List[int]):
        if len(temp) == k and tmp_sum == n:
            tmp = [item for item in temp]
            res.append(tmp)
            return
        if tmp_sum + start > n or len(temp) == k:
            return
        for i in range(start, 10):
            temp.append(i)
            self.backtracking(k, n, res, i + 1, tmp_sum + i, temp)
            temp.pop()


if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum3(3, 7)
    print(res)
