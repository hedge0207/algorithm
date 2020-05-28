def f(r):
    global cnt
    if r==N:
        cnt+=1
        return
    for i in range(N):
        if column_check[i]:
            continue
        flag = 0
        for j in range(r):
            if abs(r-j)==abs(i-cl[j]):
                flag = 1
                break
        if flag:
            continue
        column_check[i]=1
        cl.append(i)
        f(r+1)
        cl.pop()
        column_check[i]=0


N = int(input())
cnt = 0
cl = []
column_check= [0]*N
f(0)
print(cnt)