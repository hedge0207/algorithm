class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1

        for i in range(n):
            if dp[i] == 0:
                return False

            if i+nums[i] >= n:
                return True

            if dp[i+nums[i]] == 0:
                for j in range(1, nums[i]+1):
                    if i+j >= n:
                        break
                    dp[i+j] = 1
        return dp[-1] == 1