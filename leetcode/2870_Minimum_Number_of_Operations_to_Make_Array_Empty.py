from collections import Counter

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        count = Counter(nums)
        ans = 0
        for num, cnt in count.items():
            if cnt == 1:
                return -1
            ans += cnt // 3
            if cnt % 3:
                ans += 1
        return ans