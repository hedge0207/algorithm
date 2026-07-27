class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        is_special_char = {}
        for char in word:
            if 97 <= ord(char) <= 122:
                if is_special_char.get(char) is None:
                    is_special_char[char] = 0
                elif is_special_char[char] == 1:
                    is_special_char[char] = 2
            elif 65 <= ord(char) <= 90:
                if is_special_char.get(char.lower()) == 0:
                    is_special_char[char.lower()] = 1
                elif is_special_char.get(char.lower()) is None:
                    is_special_char[char.lower()] = 2
        cnt = 0
        for num in is_special_char.values():
            if num == 1:
                cnt += 1
        return cnt