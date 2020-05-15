import sys
sys.stdin=open("5209_input.txt",'r')

def f(k,t):
    global ans
    if k==N:
        if ans>t:
            ans=t
        return
    if t>ans:
        return
    for i in range(N):
        if selected[i]==0:
            selected[i]=1
            f(k+1,t+cost[k][i])
            selected[i]=0

for tc in range(1,int(input())+1):
    N = int(input())
    cost = [list(map(int,input().split())) for _ in range(N)]
    ans =0xffffff
    selected = [0]*N
    f(0,0)
    print("#{} {}".format(tc,ans))