from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        need = float("-inf")
        for num in nums:
            need = max(need, num)
            ans += need - num
            need += 1
        return ans