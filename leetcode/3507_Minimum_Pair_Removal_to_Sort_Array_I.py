class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        ans = 0
        while len(nums) > 1:
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    break
            else:
                break

            min_sum_idx = 0
            min_sum = float("inf")
            for i in range(1, len(nums)):
                if nums[i]+nums[i-1] < min_sum:
                    min_sum_idx = i
                    min_sum = nums[i]+nums[i-1]
            nums = nums[:min_sum_idx-1] + [min_sum] + nums[min_sum_idx+1:]
            ans += 1
        return ans