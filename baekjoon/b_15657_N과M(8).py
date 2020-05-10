def f(k,c):
    if k==M:
        for i in l:
            print(i,end=" ")
        print()
    else:
        for i in range(c,len(arr)):
            l.append(arr[i])
            f(k+1,i)
            l.pop()


N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

l=[]
f(0,0)