def f(k,c):
    global S
    if k==6:
        print(' '.join(map(str,l)))
        return
    for i in range(c,len(S)):
        if visited[i]==0:
            visited[i]=1
            l.append(S[i])
            f(k+1,i)
            visited[i]=0
            l.pop()

while 1:
    arr = list(map(int,input().split()))
    if arr == [0]:
        break
    n = arr[0]
    S = []
    l = []
    for i in range(1,len(arr)):
        S.append(arr[i])
    visited = [0] * len(S)
    f(0,0)
    print()
