years = list(map(int, input().split()))
nums = [15, 28, 19]

num = 1
while 1:
    for i in range(3):
        if num % nums[i] != years[i]:
            if num % nums[i] == 0 and years[i] == nums[i]:
                continue
            break
    else:
        break
    num += 1
print(num)