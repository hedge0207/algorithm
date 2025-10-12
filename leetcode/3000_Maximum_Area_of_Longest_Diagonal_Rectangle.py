class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_val = 0
        ans = 0
        for dimension in dimensions:
            w, h = dimension
            diagonal_square = w**2 + h**2
            if diagonal_square > max_val:
                max_val = diagonal_square
                ans = w * h
            elif diagonal_square == max_val:
                ans = max(ans, w * h)
        return ans