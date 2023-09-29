from typing import List

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st, ed = 0, len(nums)
        while st < ed:
            mid = (st + ed) // 2
            if nums[mid] >= target:
                ed = mid
            else:
                st = mid + 1
        lower_bound = st

        st, ed = 0, len(nums)
        while st < ed:
            mid = (st + ed) // 2
            if nums[mid] > target:
                ed = mid
            else:
                st = mid + 1
        upper_bound = st

        if lower_bound > upper_bound - 1:
            return [-1, -1]
        return [lower_bound, upper_bound - 1]