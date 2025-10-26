class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()

        def add(s):
            new_string = ""
            for i in range(len(s)):
                char = s[i]
                if i % 2 == 1:
                    char = chr(((ord(char) - ord('0') + a) % 10) + ord('0'))
                new_string += char
            return new_string

        def rotate(s):
            return s[-b:] + s[:-b]

        ans = s
        def recur(s):
            nonlocal ans

            added_s = add(s)
            if added_s not in seen:
                seen.add(added_s)
                if ans > added_s:
                    ans = added_s
                recur(added_s)

            rotated_s = rotate(s)
            if rotated_s not in seen:
                seen.add(rotated_s)
                if ans > rotated_s:
                    ans = rotated_s
                recur(rotated_s)

        recur(s)
        return ans