n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())

st, ed, ans = 0, n - 1, 0

while st < ed:
    sum_ = nums[st] + nums[ed]
    if sum_ == x:
        ans += 1
        st += 1
        ed -= 1
    elif sum_ > x:
        ed -= 1
    else:
        st += 1
print(ans)
