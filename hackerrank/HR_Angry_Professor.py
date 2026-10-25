def angryProfessor(k, a):
    arrived = 0
    for t in a:
        if t <= 0:
            arrived += 1
            if arrived == k:
                return "NO"
    return "YES"
