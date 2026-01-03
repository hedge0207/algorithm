class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ans = False
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        n, m = len(board), len(board[0])
        visited = [[0] * m for _ in range(n)]

        def dfs(d, r, c, chars):
            nonlocal ans
            if d == len(word):
                if chars == word:
                    ans = True
                return

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if ans:
                    break
                if visited[nr][nc] == 1:
                    continue
                if board[nr][nc] != word[d]:
                    continue
                visited[nr][nc] = 1
                dfs(d+1, nr, nc, chars+board[nr][nc])
                visited[nr][nc] = 0

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    dfs(1, i, j, board[i][j])
                    visited[i][j] = 0
                if ans:
                    return True
        return False