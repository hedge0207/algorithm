from typing import List


class Solution:
    def _binary_search(self, target, nums):
        st, ed = 0, len(nums) - 1

        while st <= ed:
            mid = (st + ed) // 2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                st = mid + 1
            else:
                ed = mid - 1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        result = []
        for num in nums1:
            if num in result:
                continue
            if self._binary_search(num, nums2):
                result.append(num)

        return result
