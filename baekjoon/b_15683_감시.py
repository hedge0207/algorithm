import sys
from copy import deepcopy

def recursion(d, area):
    global min_blind_spots

    if d == len(cctvs):
        cnt = 0
        for row in area:
            cnt += row.count(0)
        min_blind_spots = min(min_blind_spots, cnt)
        return

    x, y = cctvs[d]
    cctv_type = area[x][y]
    before_area = deepcopy(area)
    for direction in directions[cctv_type]:
        fill_spots(x, y, direction, area)
        recursion(d + 1, area)
        area = deepcopy(before_area)


def fill_spots(x, y, direction, area):
    for i in direction:
        nx = x
        ny = y
        while 1:
            nx += coord_x[i]
            ny += coord_y[i]
            if nx < 0 or nx == N or ny < 0 or ny == M:
                break

            if area[nx][ny] == 6:
                break

            if 1 <= area[nx][ny] <= 5 or area[nx][ny] == -1:
                continue
            area[nx][ny] = -1

input = sys.stdin.readline
N, M = map(int, input().split())
area = []
cctvs = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if 0 < row[j] < 6:
            cctvs.append([i, j])
    area.append(row)

coord_x = [-1, 0, 1, 0]
coord_y = [0, 1, 0, -1]

directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

min_blind_spots = float("infinity")
recursion(0, area)
print(min_blind_spots)