class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        longest = 0
        st = 0
        for ed in range(len(nums)):
            while nums[st] * k < nums[ed]:
                st += 1
            longest = max(longest, ed-st+1)

        return len(nums)-longest


# best_practice
class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0

        for r in range(len(nums)):
            if nums[r] > nums[l] * k:
                l += 1
        return l