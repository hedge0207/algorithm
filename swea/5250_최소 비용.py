import sys
sys.stdin = open("5250_input.txt", "r")

for tc in range(1, int(input()) + 1):
    N = int(input())
    mapp = [list(map(int,input().split())) for _ in range(N)]
    print(mapp)