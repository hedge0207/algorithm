from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        ans = 0
        st = 0
        count = defaultdict(int)
        for ed in range(len(nums)):
            count[nums[ed]] += 1
            while count[nums[ed]] > k:
                count[nums[st]] -= 1
                st += 1
            ans = max(ans, ed - st + 1)
        return ans