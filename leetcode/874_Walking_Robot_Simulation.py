class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        limit = 3 * 10 ** 4
        obstacles_per_row = {}
        for x, y in obstacles:
            if obstacles_per_row.get(x):
                obstacles_per_row[x].add(y)
            else:
                obstacles_per_row[x]= {y}

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        cur = [0, 0]
        dir = 0
        ans = 0
        for command in commands:
            if command == -2:
                dir -= 1
                dir %= 4
            elif command == -1:
                dir += 1
                dir %= 4
            else:
                for i in range(1, command+1):
                    nr, nc = cur[0] + dr[dir], cur[1] + dc[dir]
                    if nr < -limit or nr > limit or nc < -limit or nc > limit:
                        continue
                    if obstacles_per_row.get(nr) and nc in obstacles_per_row[nr]:
                        break
                    cur = [nr, nc]
                ans = max(ans, cur[0] ** 2 + cur[1]**2)
        return ans