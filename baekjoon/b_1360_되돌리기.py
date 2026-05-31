n = int(input())
commands = list(map(lambda x :[x[0], x[1], int(x[2])] if x[0] != "undo" else [x[0], int(x[1]), int(x[2])],
                   [input().split() for _ in range(n)]))
history = [["", 0, ""]]
for type_, var, time_ in commands:
    before = history[-1][0]
    if type_ == "type":
        history.append([before + var, time_, before])
    else:
        idx = len(history)-1
        cur = before
        while idx >= 0:
            if history[idx][1] >= time_ - var:
                cur = history[idx][2]
            else:
                break
            idx -= 1
        history.append([cur, time_, before])
print(history[-1][0])