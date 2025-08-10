class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 1
        st = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - st > k:
                ans += 1
                st = nums[i]
        return ans