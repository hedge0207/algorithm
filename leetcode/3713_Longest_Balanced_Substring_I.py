from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        for st in range(len(s)):
            counter = defaultdict(int)
            for ed in range(st, len(s)):
                counter[s[ed]] += 1
                if len(set(counter.values())) == 1:
                    ans = max(ans, ed-st+1)
        return ans