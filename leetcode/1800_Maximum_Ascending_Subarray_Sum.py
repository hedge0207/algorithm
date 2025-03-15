class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        result = 0
        sum_ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                sum_ += nums[i]
            else:
                result = max(sum_, result)
                sum_ = nums[i]
        return max(result, sum_)
