class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        def backtrack(d, n, nums, sum_):
            if sum_ == target:
                result.append(nums)
                return

            if d == n:
                return

            for i in range(d, n):
                if i > 0 and candidates[i] == candidates[i-1] and i != d:
                    continue
                if sum_ + candidates[i] > target:
                    break
                backtrack(i + 1, n, nums + [candidates[i]], sum_ + candidates[i])
        backtrack(0, len(candidates), [], 0)
        return result