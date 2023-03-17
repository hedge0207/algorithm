'''
초기상태
-visited배열 초기화
-Q생성
-시작점 enqueue

BFS는 거리 순으로 탐색을 한다.
'''

def BFS(G,v):  #그래프G, 탐색 시작점v
    visited=[0]*n  #n:정점의 개수
    queue=[]  #큐 생성
    queue.append(v)
    while queue:
        t=queue.pop(0)
        if not visited[t]:
            visited[t]=True
            visit(t) #필요한 처리를 한다.
        for i in G[t]:
            if not visited[i]:
                queue.append(i)



# new
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

start_vertex = 1
discovered = [start_vertex]
queue = [start_vertex]
while queue:
    vertex = queue.pop(0)
    for adjacent_vertex in graph[vertex]:
        if adjacent_vertex not in discovered:
            discovered.append(adjacent_vertex)
            queue.append(adjacent_vertex)

print(discovered)
