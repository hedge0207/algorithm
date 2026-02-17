class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return nums[0]
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            if i == 0 and nums[i] != nums[1+1]:
                ans = nums[i]
                break
            if i == len(nums)-1 and nums[i] != nums[i-1]:
                ans = nums[i]
                break
            if nums[i-1] != nums[i] and nums[i+1] != nums[i]:
                ans = nums[i]
                break
        return ans