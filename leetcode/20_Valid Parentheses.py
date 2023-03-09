class Solution:
    def isValid(self, s: str) -> bool:
        PARENTHESES = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for c in s:
            if c in PARENTHESES.values():
                if stack:
                    if PARENTHESES[stack.pop()] != c:
                        return False
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True