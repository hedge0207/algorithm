n = int(input())
nums = list(map(int, input().split()))
nums.sort()
st = 0
ed = n-1
min_ = float("inf")
ans_st, ans_ed = 0, n
while st < ed:
    sum_ = nums[st] + nums[ed]
    if min_ > abs(sum_):
        ans_st, ans_ed = st, ed
        min_ = abs(sum_)
    if sum_ < 0:
        st += 1
    elif sum_ > 0:
        ed -= 1
    else:
        break

print(nums[ans_st], nums[ans_ed])