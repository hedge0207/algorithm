from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(n, memo, d, k):
            if d == k:
                result.append(n)
                return

            for i in range(k):
                if memo[i] != 0:
                    continue
                memo[i] = 1
                dfs(n+[nums[i]], memo, d+1, k)
                memo[i] = 0

        result = []
        k = len(nums)
        dfs([], [0]*k, 0, k)
        return result


# best_practice

def permute(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

print(permute([1, 2, 3]))