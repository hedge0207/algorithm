from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        count = Counter(arr)
        sorted_by_cnt = sorted(count.items(), key=lambda v:v[1])
        i = 0
        while i < len(sorted_by_cnt):
            if k - sorted_by_cnt[i][1] >= 0:
                k -= sorted_by_cnt[i][1]
                i += 1
            else:
                break
        return len(sorted_by_cnt)-i