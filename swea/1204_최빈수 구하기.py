import sys
sys.stdin = open("1204_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    t = int(input())
    record = list(map(int, input().split()))

    arr = [0]*101
    for i in record:
        arr[i] += 1

    Max = 0

    for i in range(len(arr)):
        if Max < arr[i]:
            Max = arr[i]
            a=i
        elif Max == arr[i]:
            if i > a:
                a = i
    print("#{} {}".format(tc,a))
