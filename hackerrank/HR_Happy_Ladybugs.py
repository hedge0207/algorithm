def happyLadybugs(b):
    n = len(b)
    already_happy = True
    cnt = {}
    has_underscore = False
    for i in range(n):
        if b[i] == "_":
            has_underscore = True
        else:
            if cnt.get(b[i]) is None:
                cnt[b[i]] = 1
            else:
                cnt[b[i]] += 1

        if i > 0 and b[i] == b[i-1]:
            continue
        if i < n-1 and b[i] == b[i+1]:
            continue
        already_happy = False

    if already_happy:
        return "YES"

    if not has_underscore:
        return "NO"

    for color, num in cnt.items():
        if num < 2:
            return "NO"
    return "YES"