class Solution:
    def kthCharacter(self, k: int) -> str:
        def swap_next_char(char):
            return chr(ord(char) % ord("a")+ord("a")+1)

        word = "ab"
        while len(word) < k:
            word += word[len(word)//2:] + "".join([swap_next_char(char) for char in word[len(word)//2:]])

        return word[k-1]