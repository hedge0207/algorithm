class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        result = 0
        stack = []
        for i in range(len(nums)):
            if stack and nums[stack[-1]] <= nums[i]:
                idx = 1
                while len(stack) >= idx and nums[stack[-idx]] <= nums[i]:
                    result = max(i - stack[-idx], result)
                    idx += 1
            else:
                stack.append(i)
        return result