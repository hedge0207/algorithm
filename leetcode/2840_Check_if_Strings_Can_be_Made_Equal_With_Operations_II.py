class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd_even_per_char_s1 = {}
        odd_even_per_char_s2 = {}
        for i in range(len(s1)):
            if odd_even_per_char_s1.get(s1[i]) is None:
                odd_even_per_char_s1[s1[i]] = {0:0, 1:0}
            odd_even_per_char_s1[s1[i]][i%2] += 1

            if odd_even_per_char_s2.get(s2[i]) is None:
                odd_even_per_char_s2[s2[i]] = {0:0, 1:0}
            odd_even_per_char_s2[s2[i]][i % 2] += 1

        for char in s1:
            if odd_even_per_char_s2.get(char) is None:
                return False
            if odd_even_per_char_s1[char] != odd_even_per_char_s2[char]:
                return False
        return True


# best_practice
from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and \
               Counter(s1[1::2]) == Counter(s2[1::2])