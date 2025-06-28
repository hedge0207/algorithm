from collections import defaultdict


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        num_chars = defaultdict(int)

        for char in s:
            num_chars[ord(char)] += 1

        for _ in range(t):
            before = num_chars[ord("a")]
            for cd in range(ord("b"), ord("z")+1):
                before, num_chars[cd] = num_chars[cd], before
            num_chars[ord("a")] = before
            num_chars[ord("b")] += before
        return sum(num_chars.values()) % (10**9+7)