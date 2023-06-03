import sys


input = sys.stdin.readline
N, k = map(int, input().split())
coin_values = [int(input()) for _ in range(N)]

result = 0
for i in range(N - 1, -1, -1):
    value = coin_values[i]
    if k - coin_values[i] >= 0:
        result += k // value
        k %= value

    if k == 0:
        print(result)
        break
