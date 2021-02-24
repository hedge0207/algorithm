stack = []
for i in range(int(input())):
    num = int(input())
    if num:
        stack.append(num)
    else:
        if len(stack) > 0:
            stack.pop()
result = 0
for i in stack:
    result += i

print(result)
