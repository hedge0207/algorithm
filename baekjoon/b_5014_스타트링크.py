def f():
    global ans
    Q = [[S, 0]]
    visited = [0] * (F + 1)
    visited[S]=1

    while Q:
        NQ = []
        for cur,cnt in Q:
            if cur == G:
                ans=cnt
            if cur+U<=F and not visited[cur+U] and cur+U:
                visited[cur+U]=1
                NQ.append([cur+U,cnt+1])
            if cur-D>=1 and not visited[cur-D]:
                visited[cur-D]=1
                NQ.append([cur-D,cnt+1])
        Q=NQ


F,S,G,U,D = map(int,input().split())
ans = 0
f()

#처음에는 S==G인 경우를 생각하지 못해서 3번 틀림
#S==G인 경우를 추가해서 바로 통과
if S==G:
    print(0)
elif ans == 0:
    print("use the stairs")
else:
    print(ans)

