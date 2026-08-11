from collections import deque


class Solution:
    def processStr(self, s: str) -> str:
        result = deque()
        is_left = False
        for char in s:
            if char == "*":
                if len(result) == 0:
                    continue
                if is_left:
                    result.popleft()
                else:
                    result.pop()
            elif char == "#":
                result += result
            elif char == "%":
                is_left = not is_left
            else:
                if is_left:
                    result.appendleft(char)
                else:
                    result.append(char)

        if is_left:
            return "".join(list(result)[::-1])
        else:
            return "".join(list(result))