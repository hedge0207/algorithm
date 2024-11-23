def recursion(n, fact, i):
    if fact > n:
        return i - 1
    return recursion(n, fact * (i + 1), i + 1)

def solution(n):
    return recursion(n, 1, 1)


print(solution(2))
