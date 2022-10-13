from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False for _ in range(len(nums))]
        self.backtracking(nums, [], used, res)
        return res

    def backtracking(self,
                     nums: List[int], temp: List[int],
                     used: List[bool], res: List[List[int]]):
        if len(temp) == len(nums):
            res.append([i for i in temp])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            self.backtracking(nums, temp + [nums[i]], used, res)
            used[i] = False


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))

