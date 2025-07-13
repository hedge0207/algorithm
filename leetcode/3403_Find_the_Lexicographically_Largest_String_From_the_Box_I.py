class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        largest_char_idx = 0
        for i in range(len(word)):
            if ord(word[i]) > ord(word[largest_char_idx]):
                largest_char_idx = i
            elif ord(word[i]) == ord(word[largest_char_idx]):
                cnt = 1
                while i + cnt < len(word) and largest_char_idx+cnt < i:
                    if ord(word[i + cnt]) > ord(word[largest_char_idx + cnt]):
                        largest_char_idx = i
                        break
                    elif ord(word[i + cnt]) < ord(word[largest_char_idx + cnt]):
                        break
                    cnt += 1

        remain = numFriends
        l = 0
        r = len(word)
        for i in range(len(word)):
            remain -= 1
            if i < largest_char_idx:
                l += 1
            elif i > largest_char_idx:
                r -= 1
            if remain == 0:
                break
        if l < largest_char_idx:
            l = largest_char_idx
        return word[l:r]


























s = Solution()
# print(s.answerString("dbca", 2))
# print(s.answerString("gggg", 4))
# print(s.answerString("aadd", 3))
# print(s.answerString("chgm", 2))
# print(s.answerString("nbjnc", 2))
print(s.answerString("utauirqukfd", 2))