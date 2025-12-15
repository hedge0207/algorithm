class Solution:
    def longestPalindrome(self, s: str) -> int:
        num_char = {}
        for char in s:
            if num_char.get(char):
                num_char[char] += 1
            else:
                num_char[char] = 1

        ans = 0
        has_odd = False
        for num in num_char.values():
            if num % 2 == 0:
                ans += num
            else:
                has_odd = True
                ans += num - 1
        if has_odd:
            ans += 1
        return ans
