from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, idx, d):
            if d == k:
                result.append(nums)
                return

            for i in range(idx, n+1):
                dfs(nums + [i], i+1, d+1)

        result = []
        dfs([], 1, 0)
        return result
