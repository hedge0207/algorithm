def get_num_of_family_member(n: int, k: int) -> int:
    dp = [i for i in range(k+1)]
    for _ in range(n):
        for i in range(1, k+1):
            dp[i] = dp[i-1] + dp[i]
    return dp[-1]



tc = int(input())
for _ in range(tc):
    n = int(input())
    k = int(input())
    print(get_num_of_family_member(n, k))






















"""
2
1
3
2
3
"""