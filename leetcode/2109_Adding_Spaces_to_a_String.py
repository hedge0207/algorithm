class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        ans = ""
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                j += 1
                ans += " "
            ans += s[i]
        return ans