def extraLongFactorials(n):
    memo = [0] * (n+1)
    memo[1] = 1
    def get_factorial(n):
        if memo[n] == 0:
            num = n*get_factorial(n-1)
            memo[n] = num
        return memo[n]
    get_factorial(n)
    print(memo[n])

def extraLongFactorials(n):
    ans = 1
    for num in range(1, n+1):
        ans *= num
    print(ans)
