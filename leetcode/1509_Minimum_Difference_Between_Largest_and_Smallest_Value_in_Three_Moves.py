class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        ans = float("inf")
        j = -4
        for st in range(4):
            ed = j + st
            ans = min(ans, abs(nums[st]-nums[ed]))
        return ans