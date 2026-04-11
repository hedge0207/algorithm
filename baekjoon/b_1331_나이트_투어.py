coords = list(map(lambda cell: [int(cell[1])-1, ord(cell[0])-65], [input() for _ in range(36)]))


def check_valid_move(source, target):
    s_r, s_c = source
    t_r, t_c = target
    r_diff = abs(s_r-t_r)
    c_diff = abs(s_c-t_c)
    if (r_diff == 1 and c_diff == 2) or (r_diff==2 and c_diff==1):
        return True
    return False

visited = [[0]*6 for _ in range(6)]
visited[coords[0][0]][coords[0][1]] = 1
for i in range(1, len(coords)):
    r, c = coords[i]
    if visited[r][c] == 1:
        print("Invalid")
        break
    if not check_valid_move(coords[i-1], coords[i]):
        print("Invalid")
        break
    visited[r][c] = 1
else:
    if not check_valid_move(coords[-1], coords[0]):
        print("Invalid")
    else:
        print("Valid")