class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)//2+1):
            ans = max(ans, nums[i]+nums[-i-1])
        return ans