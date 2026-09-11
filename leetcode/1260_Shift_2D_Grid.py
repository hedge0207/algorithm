class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        arr = []
        m = len(grid[0])
        for row in grid:
            arr += row

        n = len(arr)
        k = k % n
        shifted_arr = arr[len(arr)-k:] + arr[:len(arr)-k]
        ans = []
        for i in range(0, n, m):
            ans.append(shifted_arr[i:i+m])
        return ans