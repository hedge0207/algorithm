import sys
sys.stdin = open("5250_input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    D = [[0xfffff] * N for _ in range(N)]
    D[0][0] = 0
    cnt = 0

    