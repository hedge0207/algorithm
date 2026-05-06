from collections import defaultdict


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        cols_per_row = defaultdict(list)
        num_one_per_col = defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] == 1:
                    cols_per_row[i].append(j)
                    num_one_per_col[j] += 1

        ans = 0
        for row, cols in cols_per_row.items():
            if len(cols) == 1 and num_one_per_col[cols[0]] == 1:
                ans += 1
        return ans