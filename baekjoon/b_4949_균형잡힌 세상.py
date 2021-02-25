import sys

brackets = ["(", ")", "[", "]"]
while 1:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    stack = []
    for i in s:
        if i in brackets:
            flag = True
            if i == ")" and len(stack) != 0 and stack[-1] == "(":
                stack.pop()
                flag = False
            elif i == "]" and len(stack) != 0 and stack[-1] == "[":
                stack.pop()
                flag = False
            if flag:
                stack.append(i)

    if stack:
        print("no")
    else:
        print("yes")
