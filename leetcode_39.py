from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        self.backtracking(candidates, [], 0, 0, target, res)
        return res

    def backtracking(
            self, candidates: List[int], temp: List[int],
            start: int, tmp_sum: int, target: int, res: List[List[int]]):
        if tmp_sum == target:
            res.append([i for i in temp])
            return
        i = start
        while tmp_sum+candidates[start] <= target and i < len(candidates):
            self.backtracking(
                candidates, temp+[candidates[i]], i, tmp_sum+candidates[i], target, res)
            i += 1


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 5], 8))

