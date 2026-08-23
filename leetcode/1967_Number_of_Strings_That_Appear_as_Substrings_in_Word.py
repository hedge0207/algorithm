class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        sub_strings = set()
        for i in range(len(word)):
            sub_string = ""
            for j in range(i, len(word)):
                sub_string += word[j]
                sub_strings.add(sub_string)

        ans = 0
        for pattern in patterns:
            if pattern in sub_strings:
                ans += 1
        return ans