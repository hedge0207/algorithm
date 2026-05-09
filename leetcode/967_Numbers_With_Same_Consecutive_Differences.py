class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        ans = set()
        def find_nums(stack):
            if stack[-1] >= 10 or stack[-1] < 0:
                return

            if len(stack) == n:
                ans.add(int("".join(map(str, stack))))
                return

            stack.append(stack[-1] + k)
            find_nums(stack)
            stack.pop()
            stack.append(stack[-1] - k)
            find_nums(stack)
            stack.pop()

        for i in range(1, 10):
            find_nums([i])

        return list(ans)