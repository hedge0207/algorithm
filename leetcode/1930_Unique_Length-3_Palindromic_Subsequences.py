from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = defaultdict(int)
        for i in range(len(s)):
            left[s[i]] += 1
        right = defaultdict(int)

        unique_palindrome = set()
        for i in range(len(s)):
            left[s[i]] -= 1
            if i > 0:
                right[s[i-1]] += 1
            right_set = set([char for char, num in right.items() if num > 0])
            left_set = set([char for char, num in left.items() if num > 0])
            for char in right_set & left_set:
                unique_palindrome.add(char + s[i] + char)
        return len(unique_palindrome)



# best_practice
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) <= 2:
            return 0

        chars = set(s)
        res = 0
        for ch in chars:
            first = s.find(ch)
            last = s.rfind(ch)

            if first != last:
                res += len(set(s[first + 1:last]))

        return res