class Solution:
    def minimumLength(self, s: str) -> int:
        st, ed = 0, len(s)-1
        while st < ed and s[st] == s[ed]:
            char = s[st]
            while st <= ed and char == s[st]:
                st += 1
            while st <= ed and char == s[ed]:
                ed -= 1
        return ed - st + 1