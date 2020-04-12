def dfs(visited,st):
    for i in range(1,n+1):
        if net[st][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited,i)
    if len(visited) > 1:
        return len(visited)-1
    else:
        return 0
n = int(input())
l = int(input())
net = [[0]*(n+1) for _ in range(n+1)]



for i in range(l):
    a,b = map(int, input().split())
    net[a][b]=1
    net[b][a]=1

visited = [1]

print(dfs(visited,1))