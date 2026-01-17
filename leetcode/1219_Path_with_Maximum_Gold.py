class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        def dfs(r, c, gold):
            nonlocal ans
            ans = max(ans, gold)

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if visited[nr][nc]:
                    continue
                if grid[nr][nc] == 0:
                    continue
                visited[nr][nc] = 1
                dfs(nr, nc, gold + grid[nr][nc])
                visited[nr][nc] = 0

        visited = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                visited[i][j] = 1
                dfs(i, j, grid[i][j])
                visited[i][j] = 0
        return ans