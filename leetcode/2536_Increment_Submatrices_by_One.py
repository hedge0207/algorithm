class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        for query in queries:
            y1, x1, y2, x2 = query
            for i in range(y1, y2+1):
                matrix[i][x1] += 1
                if x2+1 < n:
                    matrix[i][x2+1] -= 1

        for i in range(n):
            num = 0
            for j in range(n):
                num += matrix[i][j]
                matrix[i][j] = num
        return matrix