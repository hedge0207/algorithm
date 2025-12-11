from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_char_nums = defaultdict(int)
        for char in s1:
            s1_char_nums[char] += 1

        size = len(s1)
        s2_char_nums = defaultdict(int)
        for i in range(size):
            s2_char_nums[s2[i]] += 1

        if s1_char_nums == s2_char_nums:
            return True

        for i in range(size, len(s2)):
            s2_char_nums[s2[i-size]] -= 1
            if s2_char_nums[s2[i-size]] == 0:
                del s2_char_nums[s2[i-size]]
            s2_char_nums[s2[i]] += 1

            if s1_char_nums == s2_char_nums:
                return True
        return False