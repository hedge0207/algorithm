from collections import defaultdict


class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        left = defaultdict(int)
        right = defaultdict(int)
        left[nums[0]] += 1
        for i in range(1, len(nums)):
            right[nums[i]] += 1

        ans = 0
        for i in range(1, len(nums)-1):
            right[nums[i]] -= 1
            ans += right[nums[i]*2] * left[nums[i]*2]
            left[nums[i]] += 1
        return ans % (10**9+7)