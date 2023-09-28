from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        idx = -1
        while l <= r:
            mid = (l + r + 1) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                idx = mid
                break

        st = ed = idx
        while True:
            flag = True
            if st >= 1 and nums[st - 1] == target:
                st -= 1
                flag = False
            print(ed)
            if ed <= len(nums) - 2 and nums[ed + 1] == target:
                ed += 1
                flag = False

            if flag:
                break

        return [st, ed]
