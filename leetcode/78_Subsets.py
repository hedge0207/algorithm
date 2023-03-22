class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(subset, d, k):
            result.append(subset)
            if d == k:
                return

            for i in range(d, k):
                dfs(subset + [nums[i]], i + 1, k)

        result = []
        dfs([], 0, len(nums))
        return result