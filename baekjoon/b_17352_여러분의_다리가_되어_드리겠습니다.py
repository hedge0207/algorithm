import sys

input = sys.stdin.readline

n = int(input())

parents = [i for i in range(n+1)]

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x != parent_y:
        if parent_x > parent_y:
            parents[parent_y] = parent_x
        else:
            parents[parent_x] = parent_y

root = None
for _ in range(n-2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(2, n+1):
    if find(i-1) != find(i):
        print(i-1, i)
        break

























"""
4
1 2
1 3

2

5
1 2
2 3
4 5

8
1 2
3 4
3 5
7 8
6 7
5 2
"""
