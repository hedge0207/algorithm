def fibo(n):
    if memo[n] != 0:
        return memo[n]
    if n <= 2:
        return 1
    sub_sum = fibo(n-1) + fibo(n-2)
    memo[n] = sub_sum
    return memo[n]

n = int(input())
memo = [0] * (n+1)
print(fibo(n))

