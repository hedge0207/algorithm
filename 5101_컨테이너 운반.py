import sys
sys.stdin = open("5101_input.txt", "r")

for tc in range(1, int(input()) + 1):
    c, t = map(int, input().split())
    cw = list(map(int, input().split()))
    tw = list(map(int, input().split()))
    cw.sort(reverse=True)

    ans = 0
    for i in range(len(cw)):
        for j in range(len(tw)):
            if cw[i] <= tw[j]:
                ans+=cw[i]
                tw[j]=0
                break
    print("#{} {}".format(tc,ans))