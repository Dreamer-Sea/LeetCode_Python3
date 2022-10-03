from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        self.backtracking(candidates, [], res, target, 0, 0)
        return res

    def backtracking(self,
                     candidates: List[int], temp: List[int], res: List[List[int]],
                     target: int, start: int, tmp_sum: int):
        if tmp_sum == target:
            res.append([i for i in temp])
            return
        if start >= len(candidates) or tmp_sum > target:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i-1] == candidates[i]:
                continue
            self.backtracking(
                candidates, temp + [candidates[i]],
                res, target, i+1, tmp_sum + candidates[i])


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([2, 5, 1, 2, 2], 5))
