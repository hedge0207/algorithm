class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        monotonic_stack = []
        ans = prices[:]
        for i in range(len(prices)):
            while monotonic_stack:
                if monotonic_stack[-1][1] >= prices[i]:
                    idx, price = monotonic_stack.pop()
                    ans[idx] = price - prices[i]
                else:
                    break
            monotonic_stack.append([i, prices[i]])
        return ans