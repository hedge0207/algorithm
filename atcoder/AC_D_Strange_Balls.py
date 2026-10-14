_ = input()
balls = list(map(int, input().split()))

sum_ = 0
stack = []
for ball in balls:
    sum_ += 1
    if len(stack) == 0:
        stack.append([ball, 1])
    else:
        if stack[-1][0] == ball:
            stack[-1][1] += 1
            if stack[-1][0] == stack[-1][1]:
                sum_ -= stack.pop()[1]
        else:
            stack.append([ball, 1])
    print(sum_)