class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        digits_and_alphas = set([i for i in range(ord("a"), ord("z")+1)])
        digits_and_alphas = digits_and_alphas.union(set([i for i in range(ord("A"), ord("Z")+1)]))
        digits_and_alphas = digits_and_alphas.union(set([i for i in range(ord("0"), ord("9")+1)]))
        for char in word:
            if ord(char) not in digits_and_alphas:
                return False

        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for char in word:
            if char in vowels:
                break
        else:
            return False
        alphas = set([chr(i) for i in range(ord("A"), ord("Z")+1)]).union(set([chr(i) for i in range(ord("a"), ord("z")+1)]))
        consonants = alphas - vowels
        for char in word:
            if char in consonants:
                break
        else:
            return False

        return True



























s = Solution()
print(s.isValid("234Adas"))
print(s.isValid("b3"))
print(s.isValid("a3$e"))
print(s.isValid("Ya$"))
print(s.isValid("y0Ap"))


