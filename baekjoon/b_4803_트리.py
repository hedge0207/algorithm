import sys


def dfs(parent):
    for child in trees[parent]:
        if child == parents[parent]:
            continue
        if visited[child]:
            return False
        visited[child] = 1
        parents[child] = parent
        if not dfs(child):
            return False

    return True


input = sys.stdin.readline
case = 1
while 1:
    N, M = map(int, input().split())
    if N + M == 0:
        break
    trees = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        v1, v2 = map(int, input().split())
        trees[v1].append(v2)
        trees[v2].append(v1)

    cnt = 0
    visited = [0] * (N + 1)
    parents = [0] * (N + 1)
    for root in trees:
        if visited[root] != 0:
            continue
        visited[root] = 1
        if dfs(root):
            cnt += 1

    if cnt == 0:
        print("Case {}: No trees.".format(case))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, cnt))

    case += 1