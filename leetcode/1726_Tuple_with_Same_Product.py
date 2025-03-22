from collections import defaultdict
import math

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        result = 0
        counter = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                counter[nums[i] * nums[j]] += 1

        for cnt in counter.values():
            if cnt >= 2:
                result += 8 * math.comb(cnt, 2)
        return result