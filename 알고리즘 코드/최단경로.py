# 다익스트라+인접리스트
'''
input
6 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''

V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])

# dist(가중치), selected(선택 여부) 배열 준비
INF = float('inf')
dist = [INF] * V
selected = [False] * V

# 시작 정점 선택
dist[0] = 0
# 모든 정점이 선택될 때 까지
cnt = 0
while cnt < V:
    # dist가 최소인 정점 찾기
    Min = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] < Min:
            Min = dist[i]
            u = i
    # 결정
    selected[u] = True
    cnt += 1
    # 간선 완화
    for w, cost in adj[u]:  # w:도착 정점, cost: 가중치
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost

print(dist)
