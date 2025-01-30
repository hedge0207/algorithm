from collections import defaultdict

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        num_server_per_row = defaultdict(int)
        num_server_per_col = defaultdict(int)
        m = len(grid)
        n = len(grid[0])
        servers = []
        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                if value == 1:
                    num_server_per_row[i] += value
                    num_server_per_col[j] += value
                    servers.append([i, j])

        num_single_server = 0
        for server in servers:
            if num_server_per_row[server[0]] == 1 and num_server_per_col[server[1]] == 1:
                num_single_server += 1

        return len(servers)-num_single_server