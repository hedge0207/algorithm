class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = {}
        for char in s:
            if char in cnt:
                cnt[char] += 1
            else:
                cnt[char] = 1

        odd_char = ""
        ans = ""
        for i in range(26):
            i += 97
            char = chr(i)
            num = cnt.get(char)
            if num is None:
                continue
            if num % 2:
                odd_char = char
            ans += char * (num // 2)
        return ans + odd_char + ans[::-1]