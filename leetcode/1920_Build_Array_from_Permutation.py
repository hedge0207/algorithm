class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans
