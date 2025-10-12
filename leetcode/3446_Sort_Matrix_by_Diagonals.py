class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        ans = [[0]*n for _ in range(n)]
        for i in range(1, n):
            x, y = i, 0
            diagonal_arr = []
            while x < n and y < n:
                diagonal_arr.append(grid[y][x])
                x += 1
                y += 1
            diagonal_arr.sort()
            x, y = i, 0
            cnt = 0
            while x < n and y < n:
                ans[y][x] = diagonal_arr[cnt]
                x += 1
                y += 1
                cnt += 1
        for i in range(n):
            x, y = 0, i
            diagonal_arr = []
            while x < n and y < n:
                diagonal_arr.append(grid[y][x])
                x += 1
                y += 1
            diagonal_arr.sort(reverse=True)
            x, y = 0, i
            cnt = 0
            while x < n and y < n:
                ans[y][x] = diagonal_arr[cnt]
                x += 1
                y += 1
                cnt += 1
        return ans





























s = Solution()
print(s.sortMatrix([[1,7,3],[9,8,2],[4,5,6]]))
# print(s.sortMatrix([[0,1],[1,2]]))
# print(s.sortMatrix([[1]]))



