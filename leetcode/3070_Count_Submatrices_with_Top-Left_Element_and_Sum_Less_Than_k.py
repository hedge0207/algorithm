class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        prefix = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]
                if prefix[i][j] <= k:
                    ans += 1
        return ans