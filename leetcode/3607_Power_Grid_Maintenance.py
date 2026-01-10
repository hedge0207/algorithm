import heapq

class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        graph = {i:[] for i in range(1, c+1)}
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)

        priority_queue_per_node = {i:[] for i in range(1, c+1)}
        cnt = -1
        visited = [0] * c
        for i in graph:
            if visited[i-1]:
                continue
            priority_queue = []
            cnt += 1
            queue = [i]
            heapq.heappush(priority_queue, i)
            visited[i-1] = 1
            while queue:
                new_queue = []
                for node in queue:
                    for j in graph[node]:
                        if visited[j-1]:
                            continue
                        visited[j-1] = 1
                        new_queue.append(j)
                        heapq.heappush(priority_queue, j)
                queue = new_queue
            for node in priority_queue:
                priority_queue_per_node[node] = priority_queue

        ans = []
        is_online = [1] * c
        for op, node in queries:
            if op == 2:
                is_online[node-1] = 0
            else:
                if is_online[node-1]:
                    ans.append(node)
                else:
                    flag = True
                    while priority_queue_per_node[node]:
                        smallest_node = heapq.heappop(priority_queue_per_node[node])
                        if is_online[smallest_node-1]:
                            ans.append(smallest_node)
                            heapq.heappush(priority_queue_per_node[node], smallest_node)
                            flag = False
                            break
                    if flag:
                        ans.append(-1)
        return ans