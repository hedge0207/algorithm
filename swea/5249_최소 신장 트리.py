import sys
sys.stdin = open("5249_input.txt", "r")

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c

    key = [0xfffffff] * (V + 1)
    mst = [0] * (V + 1)

    key[0] = 0
    cnt = 0
    result = 0
    while cnt < V + 1:
        Min = 0xfffffff
        u = -1
        for i in range(V + 1):
            if not mst[i] and key[i] < Min:
                Min = key[i]
                u = i

        mst[u] = 1
        result += Min
        cnt += 1

        for i in range(V + 1):
            if key[i] > adj[u][i] and not mst[i] and adj[u][i]:
                key[i] = adj[u][i]

    print("#{} {}".format(tc, result))
