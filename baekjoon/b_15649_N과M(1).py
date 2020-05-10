N, M =map(int,input().split())
a=[]
u=[0]*(N+1)

def f(m):
    if len(a)==m:
        for i in range(m):
            print(a[i],end=" ")
        print()
    else:
        for i in range(1,N+1):
            if u[i]:
                continue
            else:
                u[i]=1
                a.append(i)
                f(m)
                u[i]=0
                a.pop()

f(M)