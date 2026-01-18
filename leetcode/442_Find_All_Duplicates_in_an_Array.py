class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        nums.sort()
        prev = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] == prev:
                ans.append(nums[i])
            prev = nums[i]
        return ans
