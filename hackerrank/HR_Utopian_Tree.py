def utopianTree(n):
    ans = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            ans += 1
        else:
            ans *= 2
    return ans
