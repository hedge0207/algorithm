N,M = map(int, input().split())
arr=sorted(list(map(int, input().split())))
a = []
u = [0]*N

def back(k,c):
    if k == M:
        for i in range(M):
            print(a[i],end=" ")
        print()
    else:
        for i in range(c,N):
            if len(a)!=0:
                if a[-1]>arr[i]:
                    continue
            if u[i]:
                continue
            else:
                u[i]=1
                a.append(arr[i])
                back(k+1,c+1)
                u[i]=0
                a.pop()

back(0,0)