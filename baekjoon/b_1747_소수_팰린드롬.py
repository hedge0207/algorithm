n = int(input())
num = n
while 1:
    if num <= 2:
        num = 2
        break
    if num % 2 == 0:
        num += 1
        continue

    if str(num) != str(num)[::-1]:
        num += 1
        continue

    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            num += 1
            break
    else:
        break
print(num)