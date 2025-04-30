class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = len(nums)
        num_set = set()

        for i in range(n-1, -1, -1):
            num = nums[i]
            if num in num_set:
                return i // 3 + 1
            num_set.add(num)
        return 0