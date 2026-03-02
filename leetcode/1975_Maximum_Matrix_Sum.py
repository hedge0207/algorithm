class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        ans = 0
        tcnt = 0
        min_ = abs(matrix[0][0])
        for i in range(n):
            cnt = 0
            for j in range(n):
                if matrix[i][j] < 0:
                    cnt += 1
                min_ = min(min_, abs(matrix[i][j]))
                ans += abs(matrix[i][j])
            if cnt % 2:
                tcnt += 1

        if tcnt % 2:
            ans -= min_*2
        return ans