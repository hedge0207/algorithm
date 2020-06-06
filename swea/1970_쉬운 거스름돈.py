import sys
sys.stdin = open("1970_input.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    Sum = 0
    ans = [0] * 8
    while True:
        for i in range(len(change)):
            if Sum + change[i] > N:
                continue
            ans[i]+=1
            Sum+=change[i]
            break

        if N-Sum<10:
            break
    print("#{}".format(tc))
    for i in ans:
        print(i,end=" ")
    print()

