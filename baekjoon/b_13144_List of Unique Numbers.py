N = int(input())
arr = list(map(int, input().split()))

ed = 0
result = 0
mark = [0]*100001
num = arr[ed]
cnt = 0

for st in range(N):
    while ed < N:
        num = arr[ed]
        if mark[num] == 1:
            break
        else:
            mark[num] = 1
            cnt += 1
        ed += 1

    result += cnt
    mark[arr[st]] = 0
    cnt -= 1

print(result)