class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        for st in range(len(sequence)):
            ed = st + len(word)
            cnt = 0
            while ed <= len(sequence):
                if sequence[st:ed] == word:
                    cnt += 1
                    st = ed
                    ed += len(word)
                else:
                    break
            ans = max(cnt, ans)
        return ans


# DP
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        dp = [0] * (n + 1)
        for i in range(m, n + 1):
            if sequence[i-m:i] == word:
                dp[i] = dp[i - m] + 1
        return max(dp)