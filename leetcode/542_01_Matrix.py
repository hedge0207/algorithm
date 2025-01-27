class Solution:
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        n, m = len(mat), len(mat[0])
        result = [[float("inf")] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]

        queue = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append([i, j, 1])
                    break

        while queue:
            nq = []
            for r, c, cnt in queue:
                for i in range(4):
                    nr, nc = r + self.dr[i], c + self.dc[i]
                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue
                    if visited[nr][nc] and result[nr][nc] <= cnt:
                        continue
                    if mat[nr][nc] == 0:
                        ncnt = 0
                    else:
                        ncnt = cnt
                    visited[nr][nc] = 1
                    result[nr][nc] = min(ncnt, result[nr][nc])
                    nq.append([nr, nc, ncnt + 1])
            queue = nq

        return result




# 시간 초과로 실패한 코드
"""
아래 코드는 먼저 0에 해당하는 좌표를 모두 찾아낸 후 찾아낸 좌표를 순서대로 순회하면서 셀의 값이 1인 각 셀까지의 거리를 구하는 방식으로 구현했다.
예를 들어 [[0, 0, 0], [0, 1, 0], [1, 1, 1]]와 같은 matrix가 있을 때, 
[0,0]에서 값이 1인 모든 셀까지의 거리 [0,1]에서 값이 1인 모든 셀까지의 거리, ..., [1, 2]에서 값이 1인 모든 셀까지의 거리를 순서대로
구해 최소 거리를 갱신하는 방식으로 풀려고 했다.

생각해보면, BFS에서 queue의 앞쪽에 위치한 좌표일수록 시작 지점과 가깝다는 것을 의미하므로, 값이 0인 모든 셀을 먼저 queue에 추가하면
굳이 최소 거리를 갱신하는 작업을 하지 않아도 되며, 이를 반영한 코드가 아래의 best practice 주석 아래에 작성된 코드이다.
"""
class Solution:
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        n, m = len(mat), len(mat[0])
        result = [[0] * m for _ in range(n)]


        starting_points = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    starting_points.append([i, j])

        for r, c in starting_points:
            visited = [[0] * m for _ in range(n)]
            queue = [[r, c]]
            cnt = 0
            while queue:
                nq = []
                cnt += 1
                for r, c in queue:
                    for i in range(4):
                        nr, nc = r + self.dr[i], c + self.dc[i]
                        if nr < 0 or nr >= n or nc < 0 or nc >= m:
                            continue
                        if visited[nr][nc]:
                            continue
                        if mat[nr][nc] == 0:
                            continue
                        visited[nr][nc] = 1
                        if result[nr][nc] == 0:
                            result[nr][nc] = cnt
                        else:
                            result[nr][nc] = min(cnt, result[nr][nc])
                        nq.append([nr, nc])
                queue = nq

        return result


# best practice
import collections

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1
        while q:
            r, c = q.popleft()
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or row == ROWS or col < 0 or col == COLS or mat[row][col] != -1:
                    continue
                mat[row][col] = mat[r][c] + 1
                q.append((row, col))
        return mat





































s = Solution()
# print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(s.updateMatrix([[0]]))
