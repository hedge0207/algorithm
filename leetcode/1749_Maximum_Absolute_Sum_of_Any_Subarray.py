class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        local_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            if local_max > global_max:
                global_max = local_max

        local_min = nums[0]
        global_min = nums[0]
        for i in range(1, len(nums)):
            local_min = min(nums[i], local_min + nums[i])
            if local_min < global_min:
                global_min = local_min
        return max(abs(global_min), global_max)