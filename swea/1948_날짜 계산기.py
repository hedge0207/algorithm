import sys
sys.stdin = open("1948_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    one = [1, 3, 5, 7, 8, 10, 12]
    zero = [4, 6, 9, 11]
    feb = [2]

    day = 1
    while True:
        if m1 == m2 and d1 == d2:
            break
        if m1 in one and d1 == 31:
            m1 += 1
            d1 = 0
        elif m1 in zero and d1 == 30:
            m1 += 1
            d1 = 0
        elif m1 in feb and d1 == 28:
            m1 += 1
            d1 = 0
        d1 += 1
        day += 1

    print("#{} {}".format(tc,day))

