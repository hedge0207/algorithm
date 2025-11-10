class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = {}
        for char in s:
            if counter.get(char):
                counter[char] += 1
            else:
                counter[char] = 1

        num_most_frequent_vowel = 0
        for vowel in ["a", "e", "i", "o", "u"]:
            num_most_frequent_vowel = max(num_most_frequent_vowel, counter.pop(vowel, 0))

        num_most_frequent_consonant = 0
        for num_consonant in counter.values():
            num_most_frequent_consonant = max(num_most_frequent_consonant, num_consonant)

        return num_most_frequent_consonant + num_most_frequent_vowel