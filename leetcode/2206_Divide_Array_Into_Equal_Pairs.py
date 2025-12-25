from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        cnt = Counter(nums)
        for freq in cnt.values():
            if freq % 2 == 1:
                return False
        return True
