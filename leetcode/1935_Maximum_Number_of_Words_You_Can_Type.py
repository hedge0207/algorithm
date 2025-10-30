class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = list(map(lambda x:set(list(x)), text.split()))
        broken_letters = set(list(brokenLetters))
        ans = 0
        for word in words:
            if word & broken_letters:
                continue
            ans += 1
        return ans