def good_interval(n):
    lower_bound = upper_bound = 1
    flag = False
    for i in range(len(nums)):
        if not flag and nums[i] >= n:
            upper_bound = nums[i] - 1
            if i > 0:
                lower_bound = nums[i - 1] + 1
            flag = True
        if nums[i] == n:
            return 0
    if not flag:
        lower_bound = nums[-1]

    ans = 0
    for i in range(lower_bound, upper_bound+1):
        for j in range(i+1, upper_bound + 1):
            if i <= n <= j:
                ans += 1
    return ans


_ = input()
nums = sorted(list(map(int, input().split())))
n = int(input())
print(good_interval(n))