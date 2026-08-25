def minimumLoss(price):
    n = len(price)
    idx_per_price = {price[i]:i for i in range(n)}
    price.sort()
    ans = float("inf")
    for i in range(1, n):
        if idx_per_price[price[i]] < idx_per_price[price[i-1]]:
            ans = min(ans, price[i]-price[i-1])
    return ans