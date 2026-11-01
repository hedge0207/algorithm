def solution(number, k):
    numbers = list(map(int, list(number)))
    stack = []
    for i in range(len(numbers)):
        while stack and k > 0:
            if stack[-1] >= numbers[i]:
                break
            stack.pop()
            k -= 1
        stack.append(numbers[i])

    for _ in range(k):
        stack.pop()

    return "".join(map(str, stack))