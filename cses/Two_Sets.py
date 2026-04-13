n = int(input())

target = n * (n+1) // 2 // 2
sum_a = 0
sum_b = 0
set_a = []
set_b = []
for i in range(n, 0, -1):
    if sum_a + i <= target:
        sum_a += i
        set_a.append(i)
    else:
        sum_b += i
        set_b.append(i)

if sum_a == sum_b:
    print("YES")
    print(len(set_a))
    for i in set_a:
        print(i, end=" ")
    print()
    print(len(set_b))
    for i in set_b:
        print(i, end=" ")
else:
    print("NO")


