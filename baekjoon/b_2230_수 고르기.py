import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

ans = float("inf")
p1 = 0
p2 = 1
while p1 < p2 and p2 < N:
    diff = abs(nums[p1] - nums[p2])
    if diff == M:
        ans = M
        break
    elif diff > M:
        ans = min(ans, diff)
        p1 += 1
        if p1 == p2:
            p2 += 1
    else:
        p2 += 1

print(ans)
