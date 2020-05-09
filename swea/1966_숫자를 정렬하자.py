import sys
sys.stdin=open("1966_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    aa = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(N-1-i):
            if aa[j] > aa[j+1]:
                aa[j], aa[j+1] = aa[j+1], aa[j]
    aaa = ""
    for i in aa:
        aaa += str(i)+" "
    print("#{} {}".format(tc, aaa))
