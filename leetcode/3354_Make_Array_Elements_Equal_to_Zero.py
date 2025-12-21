class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])

        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                left, right = prefix_sum[i], prefix_sum[-1] - prefix_sum[i]
                if left == right:
                    ans += 2
                elif abs(left - right) == 1:
                    ans += 1
        return ans