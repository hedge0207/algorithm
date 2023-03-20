class Solution:
    def dfs(self, grid, x, y):
        x_coord = [1, 0, -1, 0]
        y_coord = [0, 1, 0, -1]
        n = len(grid)
        m = len(grid[0])

        grid[x][y] = "2"

        for k in range(4):
            new_x = x + x_coord[k]
            new_y = y + y_coord[k]
            if new_x < 0 or new_x == n or new_y < 0 or new_y == m:
                continue

            if grid[new_x][new_y] == "1":
                self.dfs(grid, new_x, new_y)

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(grid, i, j)
        return cnt