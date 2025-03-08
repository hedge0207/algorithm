class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        local_maximum = nums[0]
        global_maximum = nums[0]

        for i in range(1, len(nums)):
            local_maximum = max(nums[i], local_maximum + nums[i])
            if local_maximum > global_maximum:
                global_maximum = local_maximum

        return global_maximum