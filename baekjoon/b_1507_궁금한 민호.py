import sys


def floyd():
    result = 0
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            flag = True
            for k in range(N):
                if i == k or j == k:
                    continue

                if graph[i][j] > graph[i][k] + graph[k][j]:
                    return -1

                if graph[i][j] == graph[i][k] + graph[k][j]:
                    flag = False
                    break
            if flag:
                result += graph[i][j]

    return result



input = sys.stdin.readline
N = int(input())
MAX_COST = float("infinity")
graph = [list(map(int, input().split())) for _ in range(N)]
print(floyd())
