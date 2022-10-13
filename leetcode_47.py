from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
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
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            if used[i]:
                continue
            used[i] = True
            self.backtracking(nums, temp + [nums[i]], used, res)
            used[i] = False


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
