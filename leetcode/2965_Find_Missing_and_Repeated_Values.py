class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        nums = set()
        repeated = 0
        for row in grid:
            for num in row:
                if num in nums:
                    repeated = num
                nums.add(num)

        missing = 0
        for num in range(1, len(grid)**2 + 1):
            if num not in nums:
                missing = num
                break
        return [repeated, missing]