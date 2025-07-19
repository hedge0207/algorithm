from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        equal_dict = defaultdict(set)
        for char1, char2 in zip(s1, s2):
            equal_dict[char1].add(char2)
            equal_dict[char2].add(char1)

        def find_smallest_char(char):
            nonlocal smallest_char

            if ord(char) < ord(smallest_char):
                smallest_char = char

            for euq_char in equal_dict[char]:
                if checked[ord(euq_char)-97]:
                    continue
                checked[ord(euq_char) - 97] = 1
                find_smallest_char(euq_char)

        ans = ""
        for char in baseStr:
            checked = [0]*26
            smallest_char = char
            checked[ord(char)-97] = 1
            find_smallest_char(char)
            ans += smallest_char
        return ans


# best
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(char):
            i = ord(char) - ord("a")
            while root[i] != i:
                i = root[i]
            return i

        root = list(range(26))
        for char1, char2 in zip(s1, s2):
            r1 = find(char1)
            r2 = find(char2)
            if r1 > r2:
                r1, r2 = r2, r1

            root[r2] = r1

        return "".join(chr(ord("a") + find(char)) for char in baseStr)