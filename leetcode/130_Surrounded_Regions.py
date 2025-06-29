class Solution:
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]


    def solve(self, board: list[list[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = [[0] * m for _ in range(n)]

        def bfs(q):
            while q:
                nq = []
                for r, c in q:
                    visited[r][c] = 1
                    for i in range(4):
                        nr, nc = r + self.dr[i], c + self.dc[i]

                        if n <= nr or nr < 0 or m <= nc or nc< 0:
                            continue

                        if visited[nr][nc] == 1 or board[nr][nc] == "X":
                            continue

                        nq.append([nr, nc])
                q = nq

        for i in range(m):
            queue = []
            if visited[0][i] == 0 and board[0][i] == "O":
                queue.append([0, i])

            if visited[n-1][i] == 0 and board[n-1][i] == "O":
                queue.append([n-1, i])
            bfs(queue)

        for i in range(n):
            queue = []
            if visited[i][0] == 0 and board[i][0] == "O":
                queue.append([i, 0])

            if visited[i][m-1] == 0 and board[i][m-1] == "O":
                queue.append([i, m-1])
            bfs(queue)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"

        return board