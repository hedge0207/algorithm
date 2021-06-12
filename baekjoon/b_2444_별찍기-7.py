n = int(input())

star = 1
iter_count = n * 2 - 1
for i in range(iter_count):
    print(' ' * ((iter_count - star) // 2)+ '*' * star)
    if i < n-1:
        star += 2
    else:
        star -= 2