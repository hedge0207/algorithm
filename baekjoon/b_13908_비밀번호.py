def recur(n: int, d: int, password: set):
    global ans
    if n == d:
        if known_numbers.issubset(password):
            ans += 1
        return
    for i in range(10):
        recur(n, d+1, password.union({i}))


n, m = map(int, input().split())
known_numbers = set(map(int, input().split())) if m != 0 else set()
ans = 0
recur(n, 0, set())
print(ans)