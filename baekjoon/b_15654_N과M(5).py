N,M = map(int, input().split())
arr=sorted(list(map(int, input().split())))
a = []
u = [0]*N

def back(k):
    if k == M:
        for i in range(M):
            print(a[i],end=" ")
        print()
    else:
        for i in range(N):
            if u[i]==1:
                continue
            else:
                u[i]=1
                a.append(arr[i])
                back(k+1)
                u[i]=0
                a.pop()

back(0)