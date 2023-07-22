from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        table = [0] * n
        if n <= 2:
            return max(nums)

        table[0], table[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            table[i] = max(nums[i] + table[i - 2], table[i - 1])

        return table[-1]