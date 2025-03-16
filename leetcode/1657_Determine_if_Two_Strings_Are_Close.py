from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        num_chars1 = Counter(word1)
        num_chars2 = Counter(word2)
        if set(num_chars1.keys())!=set(num_chars2.keys()):
            return False

        if sorted(list(num_chars1.values())) != sorted(list(num_chars2.values())):
            return False

        return True