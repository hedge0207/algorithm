class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []
        num = 0
        for i in range(len(nums)):
            num *= 2
            num += nums[i]
            ans.append(num % 5 == 0)
        return ans