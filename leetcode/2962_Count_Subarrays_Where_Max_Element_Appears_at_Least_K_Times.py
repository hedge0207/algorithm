class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_num = max(nums)
        ans = 0
        cnt = 0
        st = 0
        for ed in range(len(nums)):
            if nums[ed] == max_num:
                cnt += 1
            while cnt == k and st <= ed:
                ans += len(nums) - ed
                if nums[st] == max_num:
                    cnt -= 1
                st += 1
        return ans