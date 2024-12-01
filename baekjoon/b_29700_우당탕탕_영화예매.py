N, M, K = map(int, input().split())

seats = []
for _ in range(N):
    seats.append(list(map(int,input())))

cnt = 0
for i in range(N):
    for j in range(M - K + 1):
        if sum(seats[i][j:j+K]) == 0:
            cnt += 1

print(cnt)