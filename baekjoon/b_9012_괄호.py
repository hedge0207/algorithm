import sys

T = int(input())
for _ in range(T):
    brackets = sys.stdin.readline().strip()
    stack = []
    for i in brackets:
        if i == ")" and len(stack) != 0 and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)

    if stack:
        print("NO")
    else:
        print("YES")
