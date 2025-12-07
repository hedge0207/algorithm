class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        sum_ = 0
        ans = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            if sum_ + i > maxSum:
                continue
            sum_ += i
            ans += 1
        return ans