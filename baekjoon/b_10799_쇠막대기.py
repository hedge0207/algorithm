import sys

input = sys.stdin.readline
parentheses = input()

result = 0
stack = []
for i in range(len(parentheses)):
    parenthesis = parentheses[i]
    if parenthesis == "(":
        stack.append(parenthesis)
    else:
        stack.pop()
        if parentheses[i-1] == "(":
            result += len(stack)
        else:
            result += 1

print(result)