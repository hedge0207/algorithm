def compareTriplets(a, b):
    a_win, b_win = 0, 0
    for i, j in zip(a, b):
        if i > j:
            a_win += 1
        elif i < j:
            b_win += 1
    return f"{a_win}{b_win}"