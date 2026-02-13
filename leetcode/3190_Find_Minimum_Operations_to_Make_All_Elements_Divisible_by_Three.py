class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans += 1 if num % 3 else 0
        return ans
