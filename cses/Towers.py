n = int(input())
towers = list(map(int, input().split()))

ans = 1
built_towers = []
for tower in towers:
    if built_towers and built_towers[-1] > tower:
        st = 0
        ed = len(built_towers)
        while st < ed:
            mid = (st + ed) // 2
            if built_towers[mid] > tower:
                ed = mid
            else:
                st = mid + 1
        built_towers[ed] = tower
    else:
        built_towers.append(tower)
    print(built_towers)
print(len(built_towers))