import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())

people = defaultdict(int)
for _ in range(N):
    people[input().rstrip()] = 1

cnt = 0
result = []
for _ in range(N):
    human = input().rstrip()
    if people[human] == 1:
        result.append(human)
        cnt += 1

print(cnt)
for name in sorted(result):
    print(name)
