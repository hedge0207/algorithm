class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        first_row_sum, second_row_sum = sum(grid[0]), 0
        result = float("inf")
        for i in range(len(grid[0])):
            first_row_sum -= grid[0][i]
            result = min(result, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][i]
        return result
