class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        st = 0
        cnt = 1
        is_valid = [0] * len(nums)
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cnt += 1
            else:
                for j in range(st, st+cnt-k+1):
                    is_valid[j] = 1
                st = i
                cnt = 1
        for j in range(st, st + cnt - k + 1):
            is_valid[j] = 1

        for i in range(len(nums)-k):
            if is_valid[i] == 1 and is_valid[i+k] == 1:
                return True
        return False