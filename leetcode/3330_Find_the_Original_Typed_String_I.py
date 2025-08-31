class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        post_char = word[0]
        for i in range(1, len(word)):
            if word[i] == post_char:
                ans += 1
            post_char = word[i]
        return ans