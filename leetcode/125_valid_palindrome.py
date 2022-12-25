class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        print(s)
        for i, char in enumerate(s):
            if char == s[-(i + 1)]:
                continue
            else:
                return False

        return True

# solution2
# def isPalindrome(self, s: str) -> bool:
#     s = s.lower()
#     s.re.sub('[^a-z0-9]', '', s)
#     return s == s[::-1]