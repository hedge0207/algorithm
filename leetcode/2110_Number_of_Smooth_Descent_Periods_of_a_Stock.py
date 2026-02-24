class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        ans = 0
        cnt = 1
        for i in range(1, len(prices)):
            price = prices[i]
            if prices[i-1] - 1 == price:
                cnt += 1
            else:
                ans += cnt * (cnt+1) // 2
                cnt = 1
        ans += cnt * (cnt + 1) // 2
        return ans