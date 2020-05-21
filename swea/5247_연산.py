import sys
sys.stdin = open("5247_input.txt", "r")

def bfs():
    Q = []
    Q.append([N, 0])
    visited = [0] * 1000001
    while Q:
        NQ = []
        for i in Q:
            x, c = i
            if x == M:
                return c
            if x - 1 > 0 and visited[x-1]==0:
                visited[x-1]=1
                NQ.append([x - 1, c + 1])
            if x - 10 > 0 and visited[x-10]==0:
                visited[x-10]=1
                NQ.append([x - 10, c + 1])
            if x + 1 <= 1000000 and visited[x+1]==0:
                visited[x+1]=1
                NQ.append([x + 1, c + 1])
            if x * 2 <= 1000000 and visited[x*2]==0:
                visited[x*2]=1
                NQ.append([x * 2, c + 1])
        Q = NQ


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    print("#{} {}".format(tc, bfs()))
