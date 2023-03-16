import sys


input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

res = [-1]*N
s = [0]
for i in range(1, N):
    while len(s) != 0 and nums[s[-1]] < nums[i]:
        res[s.pop()] = nums[i]
    s.append(i)

for i in res:
    print(i, end=" ")