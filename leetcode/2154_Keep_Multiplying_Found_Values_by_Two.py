class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums = set(nums)
        num = original
        while num in nums:
            num *= 2
        return num
