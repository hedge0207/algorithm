from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        n, m = len(grid), len(grid[0])
        dr, dc = [0,0,-1,1], [-1,1,0,0]
        sr = sc = 0
        all_keys = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    sr, sc = i, j
                if grid[i][j].islower():
                    all_keys.add(grid[i][j])

        q = deque([(sr, sc, frozenset(), 0)])
        visited = {(sr, sc, frozenset())}

        while q:
            r, c, keys, dist = q.popleft()

            if len(keys) == len(all_keys):
                return dist

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < n and 0 <= nc < m):
                    continue

                cell = grid[nr][nc]

                if cell == "#":
                    continue
                if cell.isupper() and cell.lower() not in keys:
                    continue

                new_keys = keys
                if cell.islower():
                    new_keys = keys | {cell}

                new_keys = frozenset(new_keys)

                state = (nr, nc, new_keys)

                if state in visited:
                    continue
                visited.add(state)
                q.append((nr, nc, new_keys, dist + 1))
        return -1