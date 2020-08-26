import sys

sys.stdin = open("1219_input.txt", "r")

# 재귀 풀이
# def f(n,k,next):
#     global flag
#     if n==k:
#         return
#     if next==99:
#         flag = 1
#         return
#     for i in range(len(pairs[next])):
#         if pairs[next][i]==1 and visited[i]==0:
#             visited[i]=1
#             f(n,k+1,i)
#             visited[i]=0
#
# T = 10
# for tc in range(1,T+1):
#     tn, n = map(int,input().split())
#     #최대 2개의 갈림길이 존재하므로
#     #pairs = [[0]*100 for _ in range(100)]가 아닌
#     #pairs = [[0]*100 for _ in range(2)]로 해도 된다.
#     pairs = [[0]*100 for _ in range(100)]
#     route = list(map(int,input().split()))
#     visited = [0]*100
#
#     for i in range(0,len(route),2):
#         pairs[route[i]][route[i+1]]=1
#     flag=0
#     f(n,0,0)
#     print("#{} {}".format(tc,flag))

# 스택으로 풀이
T = 10
for tc in range(1, T + 1):
    tn, n = map(int, input().split())
    route = list(map(int, input().split()))
    adj = [[0] * 100 for _ in range(2)]
    visited = [0] * 100

    for i in range(0, len(route), 2):
        if adj[0][route[i]] == 0:
            adj[0][route[i]] = route[i + 1]
        else:
            adj[1][route[i]] = route[i + 1]
    print(adj)
    flag = 0
    stack = [0]
    while stack:
        n = stack.pop()
        visited[n] = 1
        if adj[0][n] == 99 or adj[1][n] == 99:
            flag = 1
            break
        if adj[0][n] != 0 and not visited[adj[0][n]]:
            stack.append(adj[0][n])
        if adj[1][n] != 0 and not visited[adj[1][n]]:
            stack.append(adj[1][n])
    print("#{} {}".format(tc, flag))
