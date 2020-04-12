N,M=map(int,input().split())
a=[]
u=[0]*(N+1)

def back(k):
    if k==M:
        for i in range(M):
            print(a[i],end=" ")
        print()
    else:
        for i in range(1,N+1):
            if u[i]==1:
                continue
            else:
                for j in range(1,i):
                    u[j]=1
                a.append(i)
                back(k+1)
                for j in range(1,i):
                    u[j]=0
                a.pop()
back(0)
