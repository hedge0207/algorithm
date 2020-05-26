# 인접 행렬 방식
# V, E = map(int, input().split())
# arr = [[0] * V for _ in range(V)]
# for _ in range(E):
#     u, v = map(int, input().split())
#     arr[u - 1][v - 1] = 1  # 무향 그래프이므로 양방향으로 추가해준다.
#     arr[v - 1][u - 1] = 1
# print(arr)

# input값, 첫 번째 줄에는 순서대로 V와 E의 개수가 주어지고 그 아래로 E개의 간선이 주어진다.
# 3 2
# 1 2
# 1 3



# 인접 리스트 방식
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]  # 정점은 7까지 있으므로 0번 인덱스는 비워 놓고 7번가지 표현하려면 +1을 해줘야 한다.
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)  # 유향그래프이고 만일 u에서 v로만 갈 수 있다면 u에다 만 추가 하면 된다.
    G[v].append(u)  # 무향그래프이기에 u,v를 모두 추가해야한다.


print(G)
for i in range(1, V + 1):
    print(i, G[i])


# input값, 첫 번째 줄에는 순서대로 V와 E의 개수가 주어지고 그 아래로 E개의 간선이 주어진다.