def f(k):
    global flag,ans
    if k==7 and sum(l)==100:
        ans = l[:]
        return
    if flag:
        return
    if sum(l)>=100:
        return
    for i in range(9):
        if visited[i] == 0:
            visited[i]=1
            l.append(arr[i])
            f(k+1)
            l.pop()
            visited[i]=0


arr = []
for i in range(9):
    arr.append(int(input()))
visited = [0]*9
ans = []
l = []
flag = 0

f(0)
ans.sort()
for i in ans:
    print(i)