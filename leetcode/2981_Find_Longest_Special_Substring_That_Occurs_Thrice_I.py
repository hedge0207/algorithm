from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        num_special_sub_strings = defaultdict(int)
        special_sub_string = ""
        prev = ""
        for i in range(len(s)):
            if s[i] == prev:
                special_sub_string += s[i]
            else:
                for j in range(1, len(special_sub_string)+1):
                    num_special_sub_strings[special_sub_string[:j]] += len(special_sub_string)-j+1
                special_sub_string = s[i]
            prev = s[i]
        for j in range(1, len(special_sub_string) + 1):
            num_special_sub_strings[special_sub_string[:j]] += len(special_sub_string) - j + 1

        ans = -1
        for sub_string, num in num_special_sub_strings.items():
            if num >= 3:
                ans = max(ans, len(sub_string))
        return ans