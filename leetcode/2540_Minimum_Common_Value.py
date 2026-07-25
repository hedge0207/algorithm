class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            while j < len(nums2) and nums1[i] > nums2[j]:
                j += 1
            if j >= len(nums2):
                break
            while i < len(nums1) and nums1[i] < nums2[j]:
                i += 1
        return -1