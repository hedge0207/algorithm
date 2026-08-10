def solution(order):
    stack = []
    idx = 0
    for i in range(1, len(order)+1):
        flag = True
        if i == order[idx]:
            flag = False
            idx += 1

        while stack:
            if stack[-1] == order[idx]:
                stack.pop()
                idx += 1
                flag = False
            else:
                break
        if flag:
            stack.append(i)

    return idx