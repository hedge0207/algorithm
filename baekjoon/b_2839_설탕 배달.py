sugar = int(input())
n = sugar // 5

for i in range(n, -1, -1):
    remain_sugar = sugar - 5 * i
    if remain_sugar == 0:
        print(i)
        break
    else:
        if remain_sugar % 3 == 0:
            print(i + remain_sugar // 3)
            break
else:
    print(-1)
