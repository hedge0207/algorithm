class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        right_sum = sum(nums) - nums[0]
        left_sum = 0
        ans = [abs(right_sum-left_sum)]
        for i in range(1, len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            ans.append(abs(right_sum - left_sum))
        return ans