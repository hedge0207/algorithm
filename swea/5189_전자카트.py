import sys
sys.stdin = open("5189_input.txt", "r")


def patrol(k, ans, s):
    global Min
    if k == N - 1:
        ans += area[s][0]
        if Min>ans:
            Min=ans
        return
    elif Min<ans:
        return
    else:
        for i in range(1,N):
            if area[s][i] == 0 or visited[i] == 1:
                continue
            else:
                visited[i] = 1
                patrol(k + 1, ans + area[s][i], i)
                visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    Min = 987654321
    patrol(0, 0, 0)
    print("#{} {}".format(tc,Min))

