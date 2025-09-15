class Solution(object):
    def maximumLength(self, nums, k):
        dp = [[0] * k for _ in range(k)]
        max_len = 0

        for num in nums:
            for j in range(k):
                remainder = num % k
                dp[remainder][j] = max(dp[remainder][j], dp[j][remainder] + 1)
                max_len = max(max_len, dp[remainder][j])
        return max_len