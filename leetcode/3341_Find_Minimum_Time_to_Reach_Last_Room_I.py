import heapq


class Solution:
    _dr = [1, -1, 0, 0]
    _dc = [0, 0, 1, -1]

    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dp = [[float("inf")] * m for _ in range(n)]
        dp[0][0] = 0

        heap = [(0, 0, 0)]  # (time, r, c)

        while heap:
            t, r, c = heapq.heappop(heap)

            if t > dp[r][c]:
                continue

            for i in range(4):
                nr, nc = r + self._dr[i], c + self._dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    wait = max(0, moveTime[nr][nc] - t)
                    nt = t + wait + 1
                    if nt < dp[nr][nc]:
                        dp[nr][nc] = nt
                        heapq.heappush(heap, (nt, nr, nc))

        return dp[-1][-1]
