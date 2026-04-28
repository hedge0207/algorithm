n, x = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted([[num, i] for i, num in enumerate(nums)])
st, ed = 0, n-1
ans = ""
while st < ed:
    if nums[st][0] + nums[ed][0] == x:
        ans = str(nums[st][1]+1) + " " + str(nums[ed][1]+1)
        break
    elif nums[st][0] + nums[ed][0] > x:
        ed -= 1
    else:
        st += 1
if ans:
    print(ans)
else:
    print("IMPOSSIBLE")