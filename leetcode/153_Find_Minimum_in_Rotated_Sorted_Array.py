class Solution:
    def findMin(self, nums: list[int]) -> int:
        st, ed = 0, len(nums)-1
        mid = (st+ed) // 2
        while st <= ed:
            if nums[mid] > nums[ed]:
                st = mid + 1
            else:
                ed = mid
            mid = (st+ed) // 2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if mid == 0 or mid == len(nums)-1:
                return nums[mid]