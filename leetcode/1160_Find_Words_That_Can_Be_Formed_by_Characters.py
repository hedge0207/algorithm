from collections import Counter, defaultdict


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count = Counter(chars)
        ans = 0
        for word in words:
            word_count = defaultdict(int)
            for char in word:
                if count.get(char) is None:
                    break
                word_count[char] += 1
                if word_count[char] > count[char]:
                    break
            else:
                ans += len(word)
        return ans