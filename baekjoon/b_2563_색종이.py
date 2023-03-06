N = int(input())
SIZE = 100

paper = [[0] * SIZE for _ in range(SIZE)]

result = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                result += 1

print(result)

