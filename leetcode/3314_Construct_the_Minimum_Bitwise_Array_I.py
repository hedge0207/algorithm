class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            for i in range(num):
                if i | i+1 == num:
                    ans.append(i)
                    break
            else:
                ans.append(-1)
        return ans