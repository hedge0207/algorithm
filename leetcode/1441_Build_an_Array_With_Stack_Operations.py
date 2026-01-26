class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ans = []
        stack = []
        for i in range(1, n+1):
            if i in target:
                while stack and stack[-1] not in target:
                    stack.pop()
                    ans.append("Pop")
            stack.append(i)
            ans.append("Push")
            if stack == target:
                break
        return ans