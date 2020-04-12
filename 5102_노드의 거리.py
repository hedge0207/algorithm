import sys
sys.stdin = open("5102_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    Q = []
    visited=[0]*(V+1)

    for i in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    S,E= map(int,input().split())
    Q.append(S)

    while Q:
        t = Q.pop(0)
        for i in G[t]:
            if not visited[i]:
                visited[i]=visited[t]+1
                Q.append(i)
    print("#{} {}".format(tc,visited[E]))


# DFS 정해
# import sys
# sys.stdin = open("5102_input.txt", "r")
#
# def dfs(s):
#     if D[s] >= D[E]:
#         return
#     if s == E:
#         return
#     for i in G[s]:
#         if D[i] > D[s] + 1:
#             D[i] = D[s] + 1
#             print(D)
#             dfs(i)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     G = [[] for _ in range(V + 1)]
#
#     D = [1000] * (V + 1)  # 아주 큰 값을 넣기
#     for i in range(E):
#         a, b = map(int, input().split())
#         G[a].append(b)
#         G[b].append(a)
#     print(G)
#     S, E = map(int, input().split())
#
#     D[S] = 0
#     dfs(S)
    # if D[E]<=50:
    #     print("#{} {}".format(tc, D[E]))
    # else:
    #     print("#{} {}".format(tc, 0))




#DFS 오답
# import sys
# sys.stdin = open("5102_input.txt", "r")
#
#
# def dfs(a):
#     for i in G[a]:
#         if D[i]:
#             continue
#         D[i]=D[a]+1
#         dfs(i)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     G = [[] for _ in range(V + 1)]
#     D = [0] * (V + 1)  # 아주 큰 값을 넣기
#     for i in range(E):
#         a, b = map(int, input().split())
#         G[a].append(b)
#         G[b].append(a)
#     S, E = map(int, input().split())
#     dfs(S)
#
#     print("#{} {}".format(tc,D[E]))