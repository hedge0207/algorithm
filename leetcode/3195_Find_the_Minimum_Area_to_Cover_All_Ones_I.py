class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        top, bottom, left, right = m, 0, n, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if i < top:
                        top = i
                    if i > bottom:
                        bottom = i
                    if j < left:
                        left = j
                    if j > right:
                        right = j

        right = right+1 if right > 0 else 1
        bottom = bottom+1 if bottom > 0 else 1

        return (bottom-top) * (right-left)













s = Solution()
print(s.minimumArea([[0,1,0],[1,0,1]]))
print(s.minimumArea([[1]]))

