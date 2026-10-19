class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        sum_ = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                sum_ += nums[i]
            else:
                break

        nums = set(nums)
        while sum_ in nums:
            sum_ += 1
        return sum_