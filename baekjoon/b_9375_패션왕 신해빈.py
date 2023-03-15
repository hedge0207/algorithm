import sys
from collections import defaultdict

input = sys.stdin.readline
for _ in range(int(input())):
    clothes = defaultdict(int)
    n = int(input())
    for _ in range(n):
        category = input().split()[1]
        clothes[category] += 1

    result = 0
    num_clothes = clothes.values()
    if len(num_clothes) > 1:
        result = 1
        for v in num_clothes:
            result *= v + 1
        # 전체 조합에서 아무것도 입지 않은 경우의 수 1개를 뺀다.
        print(result - 1)
    else:
        print(n)
