def solution(numbers, target):
    dp = {0: 1}
    for num in numbers:
        new_dp = {}
        for s, cnt in dp.items():
            new_dp[s+num] = new_dp.get(s+num, 0) + cnt
            new_dp[s-num] = new_dp.get(s-num, 0) + cnt
        dp = new_dp
    return dp[target]