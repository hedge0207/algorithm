class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        result = 1
        inc_cnt = 1
        dec_cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_cnt += 1
            else:
                result = max(inc_cnt, result)
                inc_cnt = 1

            if nums[i] < nums[i-1]:
                dec_cnt += 1
            else:
                result = max(dec_cnt, result)
                dec_cnt = 1
        return max(result, inc_cnt, dec_cnt)