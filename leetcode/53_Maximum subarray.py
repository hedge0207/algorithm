from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if dp[i - 1] >= 0:
                dp.append(nums[i] + dp[i - 1])
            else:
                dp.append(nums[i])

        return max(dp)