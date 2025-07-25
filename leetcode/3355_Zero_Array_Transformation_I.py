class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        diff = [0] * len(nums)
        for query in queries:
            st, ed = query
            diff[st] -= 1
            if ed + 1 < len(nums):
                diff[ed+1] += 1

        for i in range(1, len(diff)):
            diff[i] += diff[i-1]

        for num, d in zip(nums, diff):
            if num+d > 0:
                return False
        return True







s = Solution()
print(s.isZeroArray([1,0,1], [[0, 2]]))