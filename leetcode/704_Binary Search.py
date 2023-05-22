from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, ed = 0, len(nums) - 1
        idx = -1
        while st <= ed:
            mid = (st + ed) // 2
            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] > target:
                ed = mid - 1
            else:
                st = mid + 1

        return idx