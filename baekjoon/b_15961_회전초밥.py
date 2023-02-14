# 2531 회전초밥과 동일하지만 시간 제한이 더 줄었다.
import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:k - 1]
cache = [0 for _ in range(d + 1)]
cache[c] = 1

result = 0
cnt = 1
st = 0
ed = 0

while True:
    if ed - st == k:
        cache[sushi[st]] -= 1
        if cache[sushi[st]] == 0:
            cnt -= 1
        st += 1
        if st == N:
            break
    ed += 1
    cache[sushi[ed - 1]] += 1
    if cache[sushi[ed - 1]] == 1:
        cnt += 1

    result = max(cnt, result)

print(result)