class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        idx_per_reverse_num = {}
        ans = -1
        for i in range(len(nums)):
            num = nums[i]
            if idx_per_reverse_num.get(num) is not None:
                if ans == -1:
                    ans = i-idx_per_reverse_num[num]
                else:
                    ans = min(ans, i-idx_per_reverse_num[num])
            idx_per_reverse_num[int(str(num)[::-1])] = i
        return ans