import sys
sys.stdin = open("1285_input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    record = list(map(int, input().split()))

    Min = 987654321
    for i in record:
        if Min > abs(i):
            Min = abs(i)

    cnt=0
    for i in record:
        if abs(i) == Min:
            cnt+=1
    print("#{} {} {}".format(tc,Min, cnt))
