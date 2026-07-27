class Solution:
    def isGood(self, nums: list[int]) -> bool:
        nums.sort()
        n = len(nums)
        if n == 1:
            return False
        num = 1
        for i in range(n-2):
            if num == n:
                return False
            if num != nums[i]:
                return False
            num += 1

        return nums[-1] == nums[-2] == num