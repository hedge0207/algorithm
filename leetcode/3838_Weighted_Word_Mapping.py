class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        ans = ""
        for word in words:
            word_val = 0
            for char in word:
                word_val += weights[ord(char)-97]
            ans += chr(ord("z") - word_val % 26)
        return ans