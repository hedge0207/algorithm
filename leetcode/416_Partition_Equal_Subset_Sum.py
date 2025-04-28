class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        half = sum_ // 2
        table = [False] * (half + 1)
        table[0] = True
        for num in nums:
            for i in range(half, num-1, -1):
                table[i] = table[i-num] or table[i]
        return table[-1]