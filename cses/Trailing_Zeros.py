n = int(input())

ans = 0
divisor = 5

while divisor <= n:
    ans += n // divisor
    divisor *= 5

print(ans)