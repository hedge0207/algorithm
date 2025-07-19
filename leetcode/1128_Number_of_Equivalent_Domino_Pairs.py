from collections import defaultdict
import math

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        pairs = defaultdict(int)
        for domino in dominoes:
            concated_domino = "".join(map(str, sorted(domino)))
            pairs["".join(concated_domino)] += 1

        ans = 0
        for num in pairs.values():
            if num > 1:
                ans += math.comb(num, 2)
        return ans