class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        result = 0
        bought_price = -1
        for i in range(days):
            cur_price = prices[i]
            if bought_price == -1 or cur_price <= bought_price:
                bought_price = cur_price
                continue

            if i != days - 1:
                if prices[i + 1] < cur_price:
                    result += cur_price - bought_price
                    bought_price = -1
            else:
                result += cur_price - bought_price

        return result