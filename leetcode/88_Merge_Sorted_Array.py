from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i, j = m-1, n-1
        cur_idx = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[cur_idx] = nums1[i]
                i -= 1
            else:
                nums1[cur_idx] = nums2[j]
                j -= 1
            cur_idx -= 1
        
        print(nums1)

    
s = Solution()
s.merge([0], 0, [1], 1)
s.merge([1], 1, [], 0)
s.merge([1, 2, 3, 0, 0, 0], 3, [2,5,6], 3)