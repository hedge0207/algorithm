import sys
sys.stdin = open("1940_input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ts = [list(map(int, input().split())) for _ in range(N)]

    dis = 0
    sp = 0
    for i in range(N):
        if ts[i][0] == 0:
            dis += sp
        elif ts[i][0] == 1:
            sp += ts[i][1]
            dis += sp
        elif ts[i][0] == 2:
            if sp != 0:
                sp -= ts[i][1]
                dis += sp
            else:
                dis += sp
    print("#{} {}".format(tc, dis))


