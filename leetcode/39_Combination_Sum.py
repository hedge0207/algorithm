class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, idx):
            sum_ = sum(nums)
            if sum_ >= target:
                if sum_ == target:
                    result.append(nums)
                return

            for i in range(idx, size):
                dfs(nums + [candidates[i]], i)

        size = len(candidates)
        result = []
        dfs([], 0)

        return result