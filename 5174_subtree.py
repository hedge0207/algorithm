import sys
sys.stdin=open("5174_input.txt","r")

def subtree(N):
    global cnt
    if N == 0:
        return
    cnt += 1
    subtree(L[N])
    subtree(R[N])


for tc in range(1,int(input())+1):
    E,N = map(int,input().split())
    pair = list(map(int,input().split()))
    R = [0]*(E+2)
    L = [0]*(E+2)
    for i in range(0,len(pair),2):
        if L[pair[i]]:
            R[pair[i]]=pair[i+1]
        else:
            L[pair[i]]=pair[i+1]

    cnt=0
    subtree(N)
    print("#{} {}".format(tc,cnt))




