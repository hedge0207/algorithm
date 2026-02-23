class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        if len(buildings) < 5:
            return 0
        sorted_by_x = sorted(buildings, key=lambda x:x[0])
        min_max_per_y = {}
        for i in range(len(buildings)):
            x, y = sorted_by_x[i]
            if min_max_per_y.get(y):
                min_max_per_y[y]["max"] = x
            else:
                min_max_per_y[y] = {"min":x}

        sorted_by_y = sorted(buildings, key=lambda x: x[1])
        min_max_per_x = {}
        for i in range(len(buildings)):
            x, y = sorted_by_y[i]
            if min_max_per_x.get(x):
                min_max_per_x[x]["max"] = y
            else:
                min_max_per_x[x] = {"min": y}

        ans = 0
        for i in range(len(buildings)):
            x, y = buildings[i]
            if len(min_max_per_y[y]) == 1 or len(min_max_per_x[x]) == 1:
                continue
            if min_max_per_y[y]["min"] < x < min_max_per_y[y]["max"] and min_max_per_x[x]["min"] < y < min_max_per_x[x]["max"]:
                ans += 1
        return ans


