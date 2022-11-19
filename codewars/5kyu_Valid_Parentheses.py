def valid_parentheses(string):
    is_valid = False
    stack = []
    for parenthesis in string:
        if parenthesis == ")":
            if not stack or not stack.pop():
                return is_valid
        elif parenthesis == "(":
            stack.append(parenthesis)

    if len(stack) == 0:
        is_valid = True

    return is_valid


print(valid_parentheses("(())((()())())"))


# best practice
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
