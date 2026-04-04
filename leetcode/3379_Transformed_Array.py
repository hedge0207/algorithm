class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        result = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                result[i] = nums[(i+nums[i])%len(nums)]
        return result