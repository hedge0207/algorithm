import sys
sys.stdin = open("1946_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    aaa = ""
    for i in range(N):
        c1, k1 = input().split()
        for j in range(int(k1)):
            aaa += c1

    print("#{}".format(tc))
    for i in range(len(aaa)):
        if i == 10 or i % 10 == 0 and i != 0:
            print()
        print(aaa[i], end="")
    print()