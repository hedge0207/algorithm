class Solution:
    _dr = [1, -1, 0, 0]
    _dc = [0, 0, 1, -1]

    def findMaxFish(self, grid: list[list[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def bfs(queue: list[list[int]]):
            ans = 0
            while queue:
                new_queue = []
                for r, c, in queue:
                    ans += grid[r][c]
                    for i in range(4):
                        nr, nc = r + self._dr[i], c + self._dc[i]
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            continue

                        if grid[nr][nc] == 0 or visited[nr][nc] == 1:
                            continue

                        new_queue.append([nr, nc])
                        visited[nr][nc] = 1
                queue = new_queue
            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and visited[i][j] == 0:
                    visited[i][j] = 1
                    result = max(result, bfs([[i, j]]))

        return result