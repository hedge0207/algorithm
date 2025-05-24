class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        ans = 0
        num_distinct_elements = len(set(nums))
        n = len(nums)
        for i in range(n):
            subset = set()
            for j in range(i, n):
                subset.add(nums[j])
                if len(subset) == num_distinct_elements:
                    ans += n-j
                    break
        return ans
