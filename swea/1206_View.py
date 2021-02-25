import sys

sys.stdin = open("1206_input.txt", "r")

idx = [-2, -1, 1, 2]

for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    t_cnt = 0
    for i in range(2, N - 2):
        max_height = -1
        for j in idx:
            if buildings[i + j] > max_height:
                max_height = buildings[i + j]
            if j == 2 and buildings[i] > max_height:
                t_cnt += buildings[i] - max_height

    print("#{} {}".format(test_case,t_cnt))
