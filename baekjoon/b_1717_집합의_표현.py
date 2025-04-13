n, m = map(int, input().split())
parent = [i for i in range(n+1)]
size = [1] * (n+1)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if size[root_x] > size[root_y]:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
        else:
            parent[root_x] = root_y
            size[root_y] += size[root_x]


for _ in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
























"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

"""