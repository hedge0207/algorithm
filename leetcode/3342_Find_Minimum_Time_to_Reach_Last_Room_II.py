import heapq


class Solution:
    _dr = [0, 0, 1, -1]
    _dc = [1, -1, 0, 0]

    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dist = [[float("inf")] * m for _ in range(n)]
        dist[0][0] = 0
        queue = [(0, 1, 0, 0)]

        while queue:
            w, move_time, r, c = heapq.heappop(queue)
            if dist[r][c] != w:
                continue

            if r == n-1 and c == m-1:
                return w

            for i in range(4):
                nr = r + self._dr[i]
                nc = c + self._dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                if dist[nr][nc] < float("inf"):
                    continue

                if dist[r][c] + move_time <= moveTime[nr][nc] + move_time:
                    nw = moveTime[nr][nc] + move_time
                    dist[nr][nc] = min(nw, dist[nr][nc])
                    heapq.heappush(queue, (nw, 2 if move_time == 1 else 1, nr, nc))
                else:
                    nw = dist[r][c] + move_time
                    dist[nr][nc] = min(nw, dist[nr][nc])
                    heapq.heappush(queue, (nw, 2 if move_time == 1 else 1, nr, nc))