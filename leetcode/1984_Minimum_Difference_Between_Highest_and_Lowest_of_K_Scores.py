class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = float("inf")
        for st in range(len(nums)-k+1):
            ans = min(nums[st+k-1]-nums[st], ans)
        return ans