def solution(orders, course):
    combination = {}
    def recur(order, i, menu):
        if i == len(order):
            if len(menu) < 2:
                return
            if combination.get(menu):
                combination[menu] += 1
            else:
                combination[menu] = 1
            return

        recur(order, i+1, menu + order[i])
        recur(order, i+1, menu)

    for order in orders:
        recur(sorted(order), 0, "")

    menu_per_len = {num:{"max_":0, "menu": []} for num in course}
    for menu, cnt in combination.items():
        if len(menu) not in course or cnt < 2:
            continue
        if cnt > menu_per_len[len(menu)]["max_"]:
            menu_per_len[len(menu)]["max_"] = cnt
            menu_per_len[len(menu)]["menu"] = [menu]
        elif cnt == menu_per_len[len(menu)]["max_"]:
            menu_per_len[len(menu)]["menu"].append(menu)

    ans = []
    for val in menu_per_len.values():
        ans += val["menu"]

    return sorted(ans)