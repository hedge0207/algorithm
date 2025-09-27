from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        buckets = defaultdict(int)
        buckets[fruits[0]] = 1
        st = 0
        ans = 1
        for ed in range(1, len(fruits)):
            buckets[fruits[ed]] += 1
            while len(buckets) > 2:
                buckets[fruits[st]] -= 1
                if buckets[fruits[st]] == 0:
                    buckets.pop(fruits[st])
                st += 1
            ans = max(ans, ed - st + 1)
        return ans
