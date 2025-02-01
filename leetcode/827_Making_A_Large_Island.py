class Solution:
    _dx = [-1, 1, 0, 0]
    _dy = [0, 0, -1, 1]

    def largestIsland(self, grid: list[list[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                all_queue = []
                if grid[i][j] == 1 and visited[i][j] == 0:
                    cnt += 1
                    queue = [[i, j]]
                    visited[i][j] = cnt
                    all_queue = [[i, j]]
                    while queue:
                        new_queue = []
                        for x, y in queue:
                            for k in range(4):
                                nx, ny = x + self._dx[k], y + self._dy[k]
                                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                    continue
                                if grid[nx][ny] != 1 or visited[nx][ny] != 0:
                                    continue
                                new_queue.append([nx, ny])
                                visited[nx][ny] = cnt
                        queue = new_queue
                        all_queue += new_queue

                result = max(result, len(all_queue))
                for x, y in all_queue:
                    grid[x][y] = len(all_queue)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    sum_ = 1
                    added = set()
                    for i in range(4):
                        nx, ny = x + self._dx[i], y + self._dy[i]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if grid[nx][ny] == 0 or visited[nx][ny] in added:
                            continue

                        added.add(visited[nx][ny])
                        sum_ += grid[nx][ny]
                    result = max(sum_, result)
        return result

































s = Solution()
print(s.largestIsland([[1, 0], [0, 1]]))
# print(s.largestIsland([[1, 1], [1, 0]]))
# print(s.largestIsland([[1, 1], [1, 1]]))
# print(s.largestIsland([[0, 0], [0, 0]]))
# print(s.largestIsland([[0,1,1], [1, 0, 1], [1,1,0]]))
