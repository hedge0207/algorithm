from typing import List

class Solution:
    operators = ["+", "-", "*"]

    def compute(self, left, operator, right):
        return eval("{}{}{}".format(left, operator, right))

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        result = []
        for i in range(len(expression)):
            if expression[i] in self.operators:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:
                        result.append(self.compute(l, expression[i], r))
        return result