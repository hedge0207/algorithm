from collections import defaultdict, deque


def solution(n, infection, edges, k):
    tree = defaultdict(lambda : defaultdict(list))
    for s, t, p in edges:
        tree[s][p].append(t)
        tree[t][p].append(s)

    ans = 0
    def find_maximum(d, visited):
        nonlocal ans

        if k == d:
            ans = max(ans, sum(visited))
            return

        for i in range(1, 4):
            queue = deque()
            new_visited = [0] * (n+1)
            for node in range(n+1):
                if visited[node] == 1:
                    queue.append(node)
                    new_visited[node] = 1
            while queue:
                node = queue.popleft()
                for neighbor in tree[node][i]:
                    if new_visited[neighbor]:
                        continue
                    queue.append(neighbor)
                    new_visited[neighbor] = 1
            find_maximum(d+1, new_visited)
    visited = [0]*(n+1)
    visited[infection] = 1
    find_maximum(0, visited)
    return ans