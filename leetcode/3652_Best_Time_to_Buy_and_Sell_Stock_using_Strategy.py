class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        window_sum = 0
        sell_sum = 0
        ans = 0
        max_diff, idx = 0, -1
        total_sum = 0
        for i in range(len(strategy)):
            window_sum += strategy[i] * prices[i]
            total_sum += strategy[i] * prices[i]

            if i >= k:
                window_sum -= strategy[i-k] * prices[i-k]

            if i >= k // 2:
                sell_sum += prices[i]

            if i >= k:
                sell_sum -= prices[i-k//2]

            if i >= k-1 and sell_sum > window_sum:
                if sell_sum - window_sum > max_diff:
                    max_diff = sell_sum-window_sum
                    idx = i-k+1
                    ans = sell_sum

        if idx == -1:
            return total_sum

        for i in range(len(strategy)):
            if idx <= i < idx+k:
                continue
            ans += strategy[i] * prices[i]
        return ans