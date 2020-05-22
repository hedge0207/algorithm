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


'''                
초기상태
-visited배열 초기화
-Q생성
-시작점 enqueue

BFS는 거리 순으로 탐색을 한다.
'''
