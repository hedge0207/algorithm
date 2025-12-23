class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        num_zero_nums1 = nums1.count(0)
        num_zero_nums2 = nums2.count(0)
        sum_nums1 = sum(nums1)
        sum_nums2 = sum(nums2)
        min_nums1 = sum_nums1 + num_zero_nums1
        min_nums2 = sum_nums2 + num_zero_nums2
        if min_nums1 > min_nums2:
            if num_zero_nums2 == 0:
                return -1
            return min_nums1
        elif min_nums1 < min_nums2:
            if num_zero_nums1 == 0:
                return -1
            return min_nums2
        else:
            return min_nums1

