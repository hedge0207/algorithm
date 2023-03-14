import sys


input = sys.stdin.readline
N = int(input())
heights = [int(input()) for _ in range(N)]
result = [0] * N

stack = [N-1]
for i in range(N-2, -1, -1):
    cnt = 0
    while len(stack) != 0 and heights[stack[-1]] < heights[i]:
        cnt += 1
        cnt += result[stack.pop()]
    result[i] = cnt
    stack.append(i)

print(sum(result))