import sys


input = sys.stdin.readline

# 처음에는 sub list를 매번 생성하면서 풀려 했으나 시간초과가 발생
# slice 연산자가 빠르다 해도 어쨌든 list를 매번 생성하는 것이기에 속도가 느려졌던 것 같다.

N, S = map(int, input().split())
nums = list(map(int, input().split()))

if sum(nums) < S:
    print(0)
else:
    ans = float("inf")
    p1 = 0
    p2 = 0
    num_sum = nums[0]
    while p1 <= p2:
        if num_sum >= S:
            ans = min(ans, p2 - p1 + 1)
            num_sum -= nums[p1]
            p1 += 1
        else:
            p2 += 1
            if p2 == N:
                break
            num_sum += nums[p2]

    print(ans)