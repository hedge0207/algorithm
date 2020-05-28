'''
input(시작정점, 끝 정점, 가중치 순)
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# Prim 알고리즘
V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]  #인접행렬, 만일 인접 리스트로 구현하고 싶다면 아래 방식으로는 불가능, 우선순위 큐를 사용해야 한다.

for i in range(E):
    s, e, c = map(int, input().split())
    #무향 그래프
    adj[s][e] = c   #가중치 c를 넣어준다.
    adj[e][s] = c

# 가중치, 부모정점, MST 준비
INF = float('inf')  #가중치를 큰 값으로 초기화 하기 위한 값
key = [INF] * V  # 가중치
p = [-1] * V  # 부모 정점
mst = [False] * V  # MST, 선택한 정점을 저장하기 위한 리스트

# 시작점 선택: 0번 선택
key[0] = 0
cnt = 0
result = 0  #MST(가중치의 최소합)을 저장할 변수
while cnt < V:
    # 아직 MST가 아니고 key가 최소인 정점 u를 선택
    Min = INF
    u = -1  #아래에서 u를 쓰기 위해 -1로 초기화
    #for문을 돌면 가장 작은 가중치가 Min에 들어가게 되고 가중치가 가장 작은 정점이 u로 들어가게 된다.
    for i in range(V):
        if not mst[i] and key[i] < Min:   #MST가 아니고 u와의 사이에서 가중치가 현재 가중치보다 작으면
            Min = key[i] #가중치를 Min에 저장하고
            u = i  #정점 번호를 u에 저장

    # u를 MST로 선택(새로운 정점으로 선택)
    mst[u] = True
    result += Min
    cnt += 1

    # key 값을 갱신
    #u에 인접하면서 아직 MST가 아닌 정점 w에서 key[w]>u ↔ w 면(현재 저장된 가중치가 현재 선택된 정점 u와의 사이에서 가중치가 크면) 갱신
    for w in range(V):
        #가중치가 양수이고(adj[u][w]>0, 만일 가중치가 양수가 존재하면 조건을 삭제하면 된다.) MST로 선택한 적이 없으며(not mst[w]) key[w]>u ↔ w 면
        if adj[u][w]>0 and not mst[w] and key[w] > adj[u][w]:
            key[w] = adj[u][w]  #가중치를 갱신
            p[w] = u  #현재까지는 u에서 w의 거리가 가장 가까우므로 부모 정점을 u로 갱신

print(key)
print(p)
print(result)



# Prim 알고리즘(우선순위 큐로 구현, 시간이 위 코드보다 적게 걸린다)
# 우선순위 큐는 이진 힙으로 구현하는데 이진힙을 구현한 라이브러리가 heapq다.
# import heapq
#
# V, E = map(int, input().split())
# adj = {i: [] for i in range(V)}  #인접 리스트 생성
# for i in range(E):
#     s,e,c = map(int,input().split())
#     #무향 그래프
#     adj[s].append([e,c])
#     adj[e].append([s,c])
#
# #key, mst, 우선순위 큐 준비
# INF = float('inf')
# key = [INF] * V  # 가중치
# mst = [False] * V  # MST
# pq = [] #우선순위 큐
# #p 배열은 생략(넣어서 구현하려면 넣어도 된다.)
#
#
# #시작정점 선택
# key[0] = 0
# #큐에 시작 정점을 넣음, (key,정점인덱스)형태로 넣는다.
# #첫 번째 인자는 값을 어디에 넣을지(배열 정보), 두 번째 인자는 어떤 원소를 집어 넣을지를 입력(원소의 첫 번째 요소로 우선순위 판단)
# #heapq.heappush(추가할 배열,(우선순위를 판단할 원소,원소2)), 튜플이 아닌 원소 하나만 넣어도 된다. 튜플일 경우 가장 앞의 원소로 우선순위를 판단한다.
# #pq에 (가중치, 노드)를 넣는다.
# heapq.heappush(pq,(0,0))  #키를 우선순위로 하는 우선순위 큐
#
# result = 0
#
# while pq:
#     #최소값 찾기
#     #k는 key(가중치), node는 정점 인덱스
#     k,node = heapq.heappop(pq)  #우선순위 큐에서 가장 작은 값을 꺼내온다.
#
#     #이미 선택한 정점이면 continue
#     if mst[node]:
#         continue
#
#     #mst로 선택
#     mst[node] = True
#     result+=k
#
#     #key 갱신
#     #dest는 가려고 하는 노드, wt는 가중치
#     for dest,wt in adj[node]:
#         if not mst[dest] and key[dest] > wt:   #아직 선택한 정점이 아니고 가중치가 기존 가중치 보다 작으면
#             key[dest] = wt  #key 갱신
#             #큐 갱신 => 큐에 삽입된 가중치가 더 큰 데이터를 삭제하는 것이 아니라, 새로운 (key,정점)을 삽입하고 필요 없는 원소(가중치가 더 큰 원소)는 스킵
#             #어차피 heappop을 통해 나오는 데이터는 가중치가 최소인 데이터다.
#             # 따라서 우선순위 큐에 (99,1) , (11,1)이 들어있다고 하면 (11,1)이 먼저 나오게 될 것이고 1번 노드에 선택했다는 표시를 할 것이므로
#             # 다음에 (99,1)이 heappop을 통해 나오게 된다고 하더라도 위에서 if mst[node]에 결려서 continue 될 것이다.
#             heapq.heappush(pq,(key[dest],dest))
# print(result)


# KRUSKAL
# def make_set(x):
#     p[x] = x
#
#
# def find_set(x):
#     if p[x] == x:
#         return x
#     else:
#         p[x] = find_set(p[x])
#         return p[x]
#
#
# def union(x, y):
#     px = find_set(x)
#     py = find_set(y)
#     if rank[px]>rank[py]:
#         p[py] = px
#     else:
#         p[px] = py
#         if rank[px]==rank[py]:
#             rank[py]+=1
#
# V, E = map(int, input().split())
# edges = [list(map(int, input().split())) for _ in range(E)]
# # 간선을 간선가중치를 기준으로 정렬
# edges.sort(key=lambda x: x[2])
#
# # 모든 정점에 대해 집합 생성
# p = [0] * V
# rank = [0] * V
# for i in range(V):
#     make_set(i)
#
# cnt = 0  #선택된 간선의 개수를 새는 변수
# result = 0
# mst = []
# # 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될때까지
# for i in range(E):
#     #시작 정점, 끝 정점, 가중치
#     s,e,c = edges[i][0],edges[i][1],edges[i][2]
#     #사이클이면 스킵: 두 정점의 대표자가 같으면 스킵
#     if find_set(s)==find_set(e):
#         continue
#     # 간선 선택: mst에 간선 정보 더하기, 두 정점을 합친다 => union
#     result += c
#     mst.append(edges[i])
#     union(s,e)
#     cnt+=1
#     if cnt==V-1:
#         break
#
# print(result)
# print(mst)

