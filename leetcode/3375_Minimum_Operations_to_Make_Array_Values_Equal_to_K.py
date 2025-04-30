class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        result = 0
        num_set = set(nums)
        for num in num_set:
            if k > num:
                return -1
            elif k == num:
                result -=1
        return result + len(num_set)