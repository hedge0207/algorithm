class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        ans = True
        flag = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 == flag:
                ans = False
                break
            flag = nums[i] % 2
        return ans