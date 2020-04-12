N, M = map(int, input().split())
a = []
u = [0] * (N + 1)

def backtrack(k):
    if k==M:
        for i in range(M):
            print(a[i],end=" ")
        print()
    else:
        for i in range(1,N+1):
            u[i]=1
            a.append(i)
            backtrack(k+1)
            u[i]=0
            a.pop()

backtrack(0)