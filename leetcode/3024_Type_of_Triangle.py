from enum import Enum

class Triangle(Enum):
    EQUILATERAL = "equilateral"
    ISOSCELES = "isosceles"
    SCALENE = "scalene"



class Solution:
    def _is_valid_triangle(self, nums):
        for i in range(3):
            if nums[i] >= nums[(i+1) % 3] + nums[(i+2) % 3]:
                return False
        return True

    def triangleType(self, nums: list[int]) -> str:
        nums = sorted(nums)
        if nums[0] == nums[-1]:
            return Triangle.EQUILATERAL.value
        elif (nums[0] == nums[1] or nums[1] == nums[2]) and self._is_valid_triangle(nums):
            return Triangle.ISOSCELES.value
        else:
            if self._is_valid_triangle(nums):
                return Triangle.SCALENE.value

        return "none"