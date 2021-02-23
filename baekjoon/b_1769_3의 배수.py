def rec(n):
    global cnt, flag

    if len(n) == 1:
        if int(n) % 3 == 0:
            flag = 1
        return

    cnt += 1

    sn = 0
    for i in n:
        sn += int(i)

    rec(str(sn))


cnt = 0
flag = 0
rec(input())
print(cnt)
if flag:
    print("YES")
else:
    print("NO")
