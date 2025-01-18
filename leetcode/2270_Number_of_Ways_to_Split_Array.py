class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        result = 0
        total_sum = sum(nums)
        partial_sum = 0
        for i in range(len(nums)-1):
            partial_sum += nums[i]
            if total_sum - partial_sum <= partial_sum:
                result += 1
        return result