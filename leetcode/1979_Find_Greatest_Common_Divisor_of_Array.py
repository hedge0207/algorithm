class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a, b = max(nums), min(nums)
        while b:
            a, b = b, a % b
        return a