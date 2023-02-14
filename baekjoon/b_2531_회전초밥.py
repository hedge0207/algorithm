import sys

input = sys.stdin.readline

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = list(map(int, [input() for _ in range(N)]))
sushi += sushi

result = 0
st = 0
while st < N:
    ed = st+k
    sushi_to_eat = set(sushi[st:ed])
    num_sushi = len(sushi_to_eat)
    if c not in sushi_to_eat:
        num_sushi += 1
    result = max(result, num_sushi)
    st += 1

print(result)
