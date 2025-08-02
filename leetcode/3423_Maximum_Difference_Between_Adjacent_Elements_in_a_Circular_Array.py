class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        ans = -1
        for i in range(-1, len(nums)-1):
            ans = max(ans, abs(nums[i]-nums[i+1]))

        return ans