class Solution:

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n, m = len(heights), len(heights[0])
        ans = []
        is_reachable = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                visited = [[0] * m for _ in range(n)]
                queue = [[i, j]]
                new_queue = []
                reach_pacific, reach_atlantic = False, False
                while queue:
                    for r, c in queue:
                        if r == 0 or c == 0:
                            reach_pacific = True
                        if r == n - 1 or c == m - 1:
                            reach_atlantic = True
                        if is_reachable[r][c]:
                            reach_pacific = True
                            reach_atlantic = True
                            break

                        visited[r][c] = 1

                        for k in range(4):
                            nr, nc = r + self.dr[k], c + self.dc[k]
                            if nr >= n or nc >= m or nr < 0 or nc < 0:
                                continue
                            if visited[nr][nc]:
                                continue

                            if heights[nr][nc] <= heights[r][c]:
                                new_queue.append([nr, nc])

                    if reach_pacific and reach_atlantic:
                        ans.append([i, j])
                        is_reachable[i][j] = 1
                        break
                    queue = new_queue
                    new_queue = []
        return ans