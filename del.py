N,M = map(int,input().split())
a = []
u = [0]*(N+1)

def back():
    if len(a)==M:
        for i in a:
            print(i, end=" ")
        print()
    else:
        for i in range(1,N+1):
            if len(a) != 0:
                if i<a[-1]:
                    continue
            a.append(i)
            u[i]=1
            back()
            u[i]=0
            a.pop()

back()