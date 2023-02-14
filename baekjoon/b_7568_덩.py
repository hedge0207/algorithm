N = int(input())
size = [[i, list(map(int, input().split()))] for i in range(N)]
size = sorted(size, key=lambda x: sum(x[1]))

rating = {}

for i in range(N):
    rank = 1
    idx = size[i][0]
    x, y = size[i][1]
    for j in range(i+1, N):
        p, q = size[j][1]
        if x < p and y < q:
            rank += 1
    rating[idx] = rank

for i in range(N):
    print(rating.get(i), end=" ")