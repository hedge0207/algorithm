class Solution:
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    streets = [[2, 3], [0, 1], [0, 3], [0, 2], [1, 3], [1, 2]]

    def hasValidPath(self, grid: list[list[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = [[0]*m for _ in range(n)]
        visited[0][0] = 1
        ans = False
        def dfs(r, c):
            nonlocal ans

            if ans:
                return

            if r == n-1 and c == m-1:
                ans = True

            for i in self.streets[grid[r][c]-1]:
                nr, nc = r + self.dr[i], c + self.dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                if visited[nr][nc]:
                    continue

                if i == 0 and 1 not in self.streets[grid[nr][nc] - 1]:
                    continue
                if i == 1 and 0 not in self.streets[grid[nr][nc] - 1]:
                    continue
                if i == 2 and 3 not in self.streets[grid[nr][nc] - 1]:
                    continue
                if i == 3 and 2 not in self.streets[grid[nr][nc] - 1]:
                    continue
                visited[nr][nc] = 1
                dfs(nr, nc)
                visited[nr][nc] = 0
        dfs(0, 0)
        return ans