'''
input
8 10
1 2 2
1 3 3
2 4 3
2 5 5
3 6 1
4 7 4
5 6 1
5 7 1
6 8 6
7 8 2
'''*
#Prim 알고리즘과 거의 동일
def DIJKSTRA_ARRAY(s):
    D = [0xfffff] * (V + 1)  #시작정점부터 각 정점까지의 현재까지 알아낸 최단 거리
    P = [i for i in range(V + 1)]  #부모 노드를 저장할 배열(초기에는 자기 자신을 부모로)
    visit = [False] * (V + 1)   #선택 여부를 저장할 배열
    D[s] = 0  #시작점을 선택

    cnt = V
    while cnt:                              # 정점의 수 만큼 반복
        u, MIN = 0, 0xfffff                 # D[] 가 최소인 정점 찾기*
        for i in range(1, V + 1):
            if not visit[i] and D[i] < MIN:  #선택 기준이 '시작'정점에서 부터의 거리라는 것에 주의해야 한다.
                u, MIN = i, D[i]  #for문이 끝나면 u에는 거리가 가장 가까운 정점이 담기게 된다.

        #u 정점을 선택
        visit[u] = True

        # D[v]는 시작 정점에서 v정점 까지의 현재까지 알아낸 최단 거리, D[u]는 시작 정점에서 u정점 까지의 현재까지 알아낸 최단 거리
        # w는 v정점에서 u 정점까지의 최단거리
        # 즉 D[v] > D[u] + w는
        # 시작정점에서 v정점까지의 현재까지 알아낸 최단 거리 > 시작 정점에서 u정점 까지의 현재까지 알아낸 최단 거리+u정점에서 v정점까지의 최단거리
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w     #간선 완화 출발 정점에서 v정점까지의 최단 거리는 시작정점에서 u정점까지의 최단거리 + u정점에서 v정점까지의 최단거리(탐욕)
                P[v] = u       #v의 부모 노드를 u로

        cnt -= 1

    print(D[1: V + 1]) #가중치 정보
    print(P[1: V + 1]) #트리 정보
    #최단경로는 다양할 수 있기에 경로를 묻는 문제는 잘 나오지 않는다.


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]  #인접 리스트
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

DIJKSTRA_ARRAY(1)  #1은 시작 정점




#우선순위 큐로 구현한 Dijkstra
# import sys; sys.stdin = open('weighted_graph.txt')
#
# from queue import PriorityQueue
#
# def DIJKSTRA_PRIORITYQ(s):
#
#     D = [0xfffff] * (V + 1)
#     P = [i for i in range(V + 1)]
#     visit = [False] * (V + 1)
#     D[s] = 0
#     Q = PriorityQueue()
#     Q.put((0, s))
#
#     while not Q.empty():
#         d, u = Q.get()
#         if d > D[u]: continue
#
#         visit[u] = True
#         for v, w in G[u]:
#             if not visit[v] and D[v] > D[u] + w:
#                 D[v] = D[u] + w
#                 P[v] = u
#                 Q.put((D[v], v))
#
#     print(D[1: V + 1])
#     print(P[1: V + 1])
#
#
# V, E = map(int, input().split())
# G = [[] for _ in range(V + 1)]
# for i in range(E):
#     u, v, w = map(int, input().split())
#     G[u].append((v, w))
#     G[v].append((u, w))
#
# DIJKSTRA_PRIORITYQ(1)