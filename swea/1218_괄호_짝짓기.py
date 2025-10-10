T = 10

for test_case in range(1, T + 1):
    _ = int(input())
    par = input()
    pairs = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<',
    }
    stack = []
    ans = 1

    for char in par:
        if char in '({[<':
            stack.append(char)
        elif char in ')}]>':
            if stack[-1] == pairs[char]:
                stack.pop()
            else:
                stack.append(char)

    if len(stack) != 0:
        ans = 0

    print(f'#{test_case} {ans}')