class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            if i == 0:
                ans += 1
                continue
            ans += 1 + i // 8
        return ans