class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0

        def is_valid(i, j):
            is_dup = [False] * 10
            row_sum = [0] * 3
            col_sum = [0] * 3

            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    x = grid[k][l]
                    if x < 1 or x > 9: return False
                    row_sum[k - i + 1] += x
                    col_sum[l - j + 1] += x
                    if is_dup[x]:
                        return False
                    is_dup[x] = True

            if not any(is_dup[1:]):
                return False

            for sum_ in row_sum:
                if sum_ != 15:
                    return False
            for sum_ in col_sum:
                if sum_ != 15:
                    return False

            return grid[i - 1][j - 1] + grid[i + 1][j + 1] == 10 and grid[i + 1][j - 1] + grid[i - 1][j + 1] == 10

        ans = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 5 and is_valid(i, j):
                    ans += 1
        return ans



