from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, 0, [], res)
        return res

    def backtracking(self,
                     nums: List[int], start: int,
                     temp: List[int], res: List[List[int]]):
        if start > len(nums):
            return
        if len(temp) > 1:
            res.append([i for i in temp])
        used = [False for _ in range(202)]
        for i in range(start, len(nums)):
            if used[nums[i] + 100] or (len(temp) > 0 and nums[i] < temp[-1]):
                continue
            used[nums[i] + 100] = True
            self.backtracking(nums, i+1, temp + [nums[i]], res)


if __name__ == '__main__':
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))
