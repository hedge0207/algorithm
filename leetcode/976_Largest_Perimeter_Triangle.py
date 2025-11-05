class Solution:
    def _is_valid_triangle(self, x: int, y: int, z: int):
        if x + y <= z:
            return False
        if x + z <= y:
            return False
        if y + z <= x:
            return False

        return True

    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            x, y, z = nums[i-2], nums[i-1], nums[i]
            if self._is_valid_triangle(x, y, z):
                return x + y + z

        return 0