class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = {"a", "e", "i", "o", "u"}
        is_valid_word = [0]
        for i in range(len(words)):
            word = words[i]
            is_valid_word.append(is_valid_word[-1])
            if word[0] in vowels and word[-1] in vowels:
                is_valid_word[-1] += 1
        ans = []
        for st, ed in queries:
            ans.append(is_valid_word[ed+1]-is_valid_word[st])
        return ans