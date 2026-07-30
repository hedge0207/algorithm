class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set([char for char in word])
        cnt = 0
        for i in range(97, 123):
            if chr(i) in word and chr(i).upper() in word:
                cnt += 1
        return cnt