class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n = len(nums) // 2
        count = {}
        for num in nums:
            if count.get(num):
                count[num] += 1
            else:
                count[num] = 1
            if count[num] == n:
                return num
