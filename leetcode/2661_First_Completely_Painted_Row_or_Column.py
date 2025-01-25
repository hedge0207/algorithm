class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        result = 0
        n = len(mat)
        m = len(mat[0])
        num_row = [0] * n
        num_col = [0] * m

        coordinate_per_num = {}
        for i in range(n):
            for j in range(m):
                coordinate_per_num[mat[i][j]] = [i, j]

        for i, num in enumerate(arr):
            x, y = coordinate_per_num[num]
            num_row[x] += 1
            num_col[y] += 1
            if num_row[x] == m or num_col[y] == n:
                result = i
                break

        return result