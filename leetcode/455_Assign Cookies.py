from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        num_children = len(g)
        num_cookies = len(s)

        i, j = 0, 0
        while True:
            if i == num_children or j == num_cookies:
                break

            if g[i] <= s[j]:
                i += 1

            j += 1

        return i