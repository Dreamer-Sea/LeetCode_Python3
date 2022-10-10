from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        used = [False for i in range(len(nums))]
        self.backtracking(nums, 0, [], used, res)
        return res

    def backtracking(self,
                     nums: List[int], start: int, temp: List[int],
                     used: List[bool], res: List[List[int]]):
        res.append([i for i in temp])
        for i in range(start, len(nums)):
            if i > start and nums[i-1] == nums[i] and not used[i]:
                continue
            used[i] = True
            self.backtracking(nums, i+1, temp+[nums[i]], used, res)
            used[i] = False


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([4,4,4,1,4]))
