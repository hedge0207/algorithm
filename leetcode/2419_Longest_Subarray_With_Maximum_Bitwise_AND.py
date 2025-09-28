class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = nums[0]
        length = 1
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                length = 1
                ans = 1
            elif nums[i] == max_val:
                length += 1
            else:
                ans = max(ans, length)
                length = 0
        ans = max(ans, length)
        return ans
