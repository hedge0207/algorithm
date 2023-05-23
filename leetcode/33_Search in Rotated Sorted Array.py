from typing import List


class Solution:
    def _find_minumum_num(self, nums):
        st, ed = 0, len(nums) - 1
        while st < ed:
            mid = (st + ed) // 2

            if nums[mid] > nums[ed]:
                st = mid + 1
            else:
                ed = mid
        return st

    def search(self, nums: List[int], target: int) -> int:
        pivot = self._find_minumum_num(nums)

        st, ed = 0, len(nums) - 1

        while st <= ed:
            mid = (st + ed) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if nums[mid_pivot] == target:
                return mid_pivot
            elif nums[mid_pivot] < target:
                st = mid + 1
            else:
                ed = mid - 1

        return -1