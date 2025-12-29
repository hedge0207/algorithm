class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        prev_char = word[0]
        char = prev_char
        cnt = 1
        for i in range(1, len(word)):
            char = word[i]
            if prev_char == char and cnt < 9:
                cnt += 1
            else:
                ans += "{}{}".format(cnt, prev_char)
                cnt = 1
            prev_char = char
        ans += "{}{}".format(cnt, char)
        return ans