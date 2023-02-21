import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

stack = []
idx = 0
result = []

for i in range(1, N+1):
    stack.append(i)
    result.append("+")

    while stack[-1] == nums[idx]:
        stack.pop()
        idx += 1
        result.append("-")
        if len(stack)==0:
            break

if stack:
    print("NO")
else:
    for i in result:
        print(i)
