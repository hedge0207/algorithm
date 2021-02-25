N = 1000000

print(2, end=" ")
for i in range(3, N, 2):
    flag = True
    for j in range(3, i // 2 + 1, 2):
        if i % j:
            continue
        else:
            flag = False
            break
    if flag:
        print(i, end=" ")
