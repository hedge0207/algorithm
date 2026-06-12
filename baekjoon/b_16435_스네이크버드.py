n, l = map(int, input().split())
fruits = sorted(list(map(int, input().split())))

for fruit in fruits:
    if fruit <= l:
        l += 1
    else:
        break
print(l)