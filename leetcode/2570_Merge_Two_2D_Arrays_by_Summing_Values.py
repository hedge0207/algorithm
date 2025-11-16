from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        sum_val = defaultdict(int)
        for id_, val in nums1 + nums2:
            sum_val[id_] += val

        ans = []
        for id_, val in sum_val.items():
            ans.append([id_, val])

        return sorted(ans)
