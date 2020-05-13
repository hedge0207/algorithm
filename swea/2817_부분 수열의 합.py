import sys
sys.stdin = open("2817_input.txt", "r")

def ssum(s,c):
    global cnt
    if s == K:
        cnt+=1
        return
    if s>=K:
        return
    for i in range(c,N):
        if visited[i]==0:
            visited[i]=1
            ssum(s+numbers[i],i)
            visited[i]=0



for tc in range(1, int(input())+1):
    N,K = map(int,input().split())
    numbers = list(map(int,input().split()))
    visited = [0]*N
    cnt = 0
    Sum = 0
    ssum(Sum,0)

    print("#{} {}".format(tc,cnt))