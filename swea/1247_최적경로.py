import sys
sys.stdin = open("1247_input.txt", "r")

def f(r,c,k,e,s):
    global Min
    if k==e:
        if Min > s+abs(tmp[2]-r)+abs(tmp[3]-c):
            Min = s+abs(tmp[2]-r)+abs(tmp[3]-c)
        return
    if s>Min:
        return
    for i in range(len(cust)):
        if not visited[i]:
            visited[i]=1
            f(cust[i][0],cust[i][1],k+1,e,s+abs(r-cust[i][0])+abs(c-cust[i][1]))
            visited[i]=0


for tc in range(1, int(input()) + 1):
    N = int(input())
    tmp = list(map(int,input().split()))
    cust = []
    Min = 0xffffff
    for i in range(4,len(tmp),2):
        cust.append([tmp[i],tmp[i+1]])
    visited = [0]*len(cust)

    f(tmp[0],tmp[1],0,len(cust),0)

    print("#{} {}".format(tc,Min))