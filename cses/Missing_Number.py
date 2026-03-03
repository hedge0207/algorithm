n = int(input())
nums = sorted(list(map(int, input().split())))
for i in range(n-1):
    if i+1 != nums[i]:
        print(i+1)
        break
else:
    print(n)