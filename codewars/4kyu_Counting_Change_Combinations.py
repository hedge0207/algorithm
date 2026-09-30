def count_change(money, coins):
    dp = [0] * (money + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, money + 1):
            dp[i] += dp[i - coin]
    return dp[money]