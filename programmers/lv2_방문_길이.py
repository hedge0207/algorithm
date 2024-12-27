from enum import Enum


class DIR(Enum):
    U = [1, 0]
    D = [-1, 0]
    R = [0, 1]
    L = [0, -1]


def solution(dirs):
    ans = 0
    cur_x, cur_y = 0, 0
    visited = set()
    for direction in dirs:
        x, y = DIR[direction].value
        new_x, new_y = cur_x + x, cur_y + y
        if new_x < -5 or new_x > 5 or new_y < -5 or new_y > 5:
            continue
        path = "{}{}{}{}".format(cur_x, cur_y, new_x, new_y)
        reversed_path = "{}{}{}{}".format(new_x, new_y, cur_x, cur_y)
        cur_x, cur_y = new_x, new_y
        if path in visited:
            continue
        visited.add(path)
        visited.add(reversed_path)

        ans += 1

    return ans