n = int(input())
apples = sorted(list(map(int, input().split())))

ans = float("inf")
def recur(d, left_sum, right_sum):
    global ans
    if d == n:
        ans = min(ans, abs(left_sum-right_sum))
        return

    recur(d+1, left_sum + apples[d], right_sum)
    recur(d+1, left_sum, right_sum + apples[d])

recur(0, 0, 0)
print(ans)