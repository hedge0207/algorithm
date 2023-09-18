N = int(input())

cnt = 0
for num in range(1, N+1):
    flag = True
    num = str(num)
    dist = 0
    for i in range(len(num) - 1):
        if i == 0:
            dist = int(num[i]) - int(num[i + 1])

        if int(num[i]) - int(num[i + 1]) != dist:
            break
    else:
        cnt += 1
print(cnt)

