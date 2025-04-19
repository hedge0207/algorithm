from collections import defaultdict

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        dominant = 0
        counter = defaultdict(int)
        for i, num in enumerate(nums):
            counter[num] += 1
            if counter[num] > (i+1) // 2:
                dominant = num

        result = -1
        split_counter = defaultdict(int)
        for i, num in enumerate(nums):
            split_counter[num] += 1

            counter[num] -= 1
            if dominant == num and counter[dominant] > (len(nums)-i-1) // 2 and split_counter[num] > (i+1) // 2:
                result = i
                break
        return result