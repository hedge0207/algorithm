from collections import defaultdict, deque
import sys

input = sys.stdin.readline
N = int(input())
tree = defaultdict(list)

for _ in range(N - 1):
    vertex1, vertex2 = map(int, input().split())
    tree[vertex1].append(vertex2)
    tree[vertex2].append(vertex1)

parents = [0] * (N + 1)
parents[1] = 1
queue = deque([1])
while queue:
    cur = queue.popleft()
    for child in tree[cur]:
        if parents[child]:
            continue
        else:
            parents[child] = cur
            queue.append(child)

for parent in parents[2:]:
    print(parent)
