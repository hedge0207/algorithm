def stringConstruction(s):
    chars = set()
    cost = 0
    for char in s:
        if char not in chars:
            cost += 1
            chars.add(char)
    return cost
