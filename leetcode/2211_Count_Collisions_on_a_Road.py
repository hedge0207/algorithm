class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        stack = []
        for direction in directions:
            if len(stack) == 0:
                if direction != "L":
                    stack.append(direction)
                continue

            if direction != "R":
                while stack and stack[-1] == "R":
                    ans += 1
                    stack.pop()
                if direction == "L":
                    ans += 1
            stack.append(direction)
        return ans