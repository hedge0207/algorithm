from queue import PriorityQueue

class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        n = len(grid)
        m = len(grid[0])
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        visited = [[0] * m for _ in range(n)]
        result = [0] * len(queries)
        min_heap = PriorityQueue()
        total_points = 0
        min_heap.put((grid[0][0], 0, 0))
        visited[0][0] = 1
        queries = sorted(list(enumerate(queries)), key=lambda x:x[1])

        for idx, num in queries:
            while not min_heap.empty() and min_heap.queue[0][0] < num:
                v, r, c = min_heap.get()
                total_points += 1

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue

                    if visited[nr][nc] == 1:
                        continue

                    min_heap.put((grid[nr][nc], nr, nc))
                    visited[nr][nc] = 1
            result[idx] = total_points

        return result