from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        ans = 0
        max_freq = 0
        for num_freq in freq.values():
            if num_freq > max_freq:
                ans = num_freq
                max_freq = num_freq
            elif num_freq == max_freq:
                ans += num_freq

        return ans
