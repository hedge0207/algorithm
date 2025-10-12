class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = 0
        before_cnt = 0
        for i in range(n-1):
            if nums[i] == 1:
                cnt += 1
            else:
                if nums[i+1] == 0:
                    before_cnt = 0
                else:
                    before_cnt = cnt
                cnt = 0
            ans = max(ans, cnt + before_cnt)
        cnt = cnt + 1 if nums[-1] else cnt
        ans = max(ans, cnt+before_cnt)
        if all(nums):
            ans -= 1
        return ans


