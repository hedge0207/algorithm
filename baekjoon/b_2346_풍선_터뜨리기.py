n = int(input())
balloons = list(map(int, input().split()))
popped = [0] * n

i = 0
while 1:
    num = balloons[i]
    popped[i] = 1

    if all(popped):
        break

    while num != 0:
        if num > 0:
            i = (i + 1) % n
            if popped[i] == 0:
                num -= 1
        else:
            i = (i - 1) % n
            if popped[i] == 0:
                num += 1

































"""
5
3 2 1 -3 -1
"""