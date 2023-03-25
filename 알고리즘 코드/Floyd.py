# 중첩 list의 첫 번째 element는 정점, 두 번째 element는 가중치이다.
graph = {
    1: [[2, 7], [3, 3], [4, 3]],
    2: [[1, 7], [5, 15]],
    3: [[1, 3], [4, 7], [5, 28]],
    4: [[1, 3], [3, 7], [5, 10]],
    5: [[2, 15], [3, 28], [4, 10]]
}

N = len(graph)

d = []
for i in range(N+1):
    row = []
    for j in range(N+1):
        if i == j:
            weight = 0
        else:
            weight = float("infinity")
        row.append(weight)
    d.append(row)

for from_, vertex in graph.items():
    for to, weight in vertex:
        d[from_][to] = weight
        d[from_][to] = weight
        if from_ == to:
            d[from_][to] = 0

for i in d:
    print(i)

for k in range(1, N+1):
    for s in range(1, N+1):
        for t in range(1, N+1):
            if d[s][t] > d[s][k] + d[k][s]:
                d[s][t] = d[s][k] + d[k][s]

for i in d:
    print(i)

