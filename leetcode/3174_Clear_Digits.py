class Solution:
    def clearDigits(self, s: str) -> str:
        is_remained = [1]*len(s)
        for i in range(len(s)):
            if s[i].isdigit():
                j = i-1
                is_remained[i] = 0
                while 0 <= j:
                    if is_remained[j]:
                        is_remained[j] = 0
                        break
                    j -= 1

        return "".join([s[i] for i in range(len(s)) if is_remained[i]])