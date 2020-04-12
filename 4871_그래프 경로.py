import sys
sys.stdin=open("4871_input.txt", "r")


def dfs(visited,start):
    print("a")
    for i in range(1,V+1):
        if arr[start][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited,i)
    if end in visited:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        st,ed = map(int, input().split())
        arr[st][ed] = 1
    print(arr)

    start,end = map(int, input().split())

    print("#{} {}".format(tc,dfs([start],start)))
