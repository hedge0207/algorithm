def solution(topping):
    answer = 0
    older = {}
    o_cnt = 0
    for t in topping:
        if t in older:
            older[t] += 1
        else:
            older[t] = 1
            o_cnt += 1

    younger = {}
    y_cnt = 0
    for t in topping:
        older[t] -= 1
        if older[t] == 0:
            o_cnt -= 1

        if t not in younger:
            younger[t] = 1
            y_cnt += 1

        if o_cnt == y_cnt:
            answer += 1
    return answer