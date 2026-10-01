class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        min_, max_ = min(nums), max(nums)
        nums = set(nums)
        ans = []
        for num in range(min_+1, max_):
            if num not in nums:
                ans.append(num)
        return ans