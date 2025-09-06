class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        ans = []
        for num in nums:
            if num:
                ans.append(num)
        return ans + [0 for _ in range(len(nums)-len(ans))]