class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        platted = []
        for row in grid:
            platted += row
        platted.sort()
        median = platted[len(platted)//2]

        result = 0
        for num in platted:
            if abs(num-median) % x != 0:
                return -1
            result += abs(num-median) // x

        return result