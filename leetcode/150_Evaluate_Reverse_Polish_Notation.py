import math


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        def cal(op, a, b):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            else:
                if a / b > 0:
                    return math.floor(a / b)
                else:
                    return math.ceil(a / b)

        operations = {"+", "-", "*", "/"}
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operations:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(cal(tokens[i], num1, num2))
                continue
            stack.append(int(tokens[i]))
        return stack[0]