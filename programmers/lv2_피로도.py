class Solution:
    def __init__(self, dungeons, n):
        self.max_num = 0
        self._dungeons = dungeons
        self._n = n

    def dfs(self, t, d, visited):
        if d == self._n:
            self.max_num = max(visited.count(1), self.max_num)
            return

        for i in range(self._n):
            if visited[i]:
                continue
            min_t, consume_t = self._dungeons[i]
            if min_t <= t:
                visited[i] = 1
                self.dfs(t - consume_t, d + 1, visited)
                visited[i] = 0
            else:
                self.max_num = max(visited.count(1), self.max_num)


def solution(k, dungeons):
    n = len(dungeons)
    sol = Solution(dungeons, n)
    sol.dfs(k, 0, [0] * n)
    return sol.max_num