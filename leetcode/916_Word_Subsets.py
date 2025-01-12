from collections import defaultdict, Counter

class Solution:
    def get_num_per_char(self, words):
        chars = []
        for word in words:
            num_per_char = Counter(word)
            chars.append(num_per_char)
        return chars

    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        num_char_per_words1 = self.get_num_per_char(words1)
        num_char_per_words2 = defaultdict(int)
        for num_char_per_word in self.get_num_per_char(words2):
            for char, num in num_char_per_word.items():
                num_char_per_words2[char] = max(num, num_char_per_words2[char])

        result = []
        for i, num_per_chars in enumerate(num_char_per_words1):
            for char, num in num_char_per_words2.items():
                if num_per_chars.get(char) is None or num_per_chars[char] < num:
                    break
            else:
                result.append(words1[i])

        return result