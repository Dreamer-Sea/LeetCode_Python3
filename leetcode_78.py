from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, 0, [], res)
        return res

    def backtracking(self, nums: List[int], start: int, temp: List[int], res: List[List[int]]):
        res.append([i for i in temp])
        for i in range(start, len(nums)):
            self.backtracking(nums, i+1, temp + [nums[i]], res)


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
