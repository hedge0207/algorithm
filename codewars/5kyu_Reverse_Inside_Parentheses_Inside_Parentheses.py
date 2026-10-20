def reverse_in_parentheses(s):
    ans = ""
    stack = []
    reverse = False
    for char in s:
        if char != "(" and len(stack) == 0:
            ans += char
        else:
            if char == "(":
                reverse = not reverse
            if char == ")":
                sub_s = ""
                while stack:
                    past_char = stack.pop()
                    if past_char == "(":
                        sub_s = f"({sub_s})"
                        if stack:
                            stack.append(sub_s)
                        else:
                            ans += sub_s
                        break
                    if not reverse:
                        sub_s = past_char + sub_s
                    else:
                        sub_s += past_char
                reverse = not reverse
            else:
                stack.append(char)
    return ans


# best_practice
def reverse_parentheses(s: str) -> str:
    stack = [[]]

    for c in s:
        if c == '(':
            stack.append([])
        elif c == ')':
            top = stack.pop()
            top.reverse()
            top = [')' if ch == '(' else '(' if ch == ')' else ch for ch in top]
            stack[-1].append('(')
            stack[-1].extend(top)
            stack[-1].append(')')
        else:
            stack[-1].append(c)

    return ''.join(stack[0])