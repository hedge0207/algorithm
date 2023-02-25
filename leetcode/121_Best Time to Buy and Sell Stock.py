def maxProfit(prices):
    result = 0
    st = 0
    for ed in range(1, len(prices)):
        if prices[ed] < prices[st]:
            st = ed

        if prices[ed] > prices[st]:
            result = max(result, prices[ed]-prices[st])

    return result

maxProfit([2,42,7,1,5,3,6,4])