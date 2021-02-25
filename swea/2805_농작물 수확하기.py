import sys

sys.stdin = open("2805_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    result = 0

    for i in range(-(N // 2), N // 2 + 1):
        for j in range(-(N // 2), N // 2 + 1):
            if abs(i) + abs(j) > N // 2:
                continue
            result += farm[N // 2 + i][N // 2 + j]

    print("#{} {}".format(tc, result))