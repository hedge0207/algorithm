class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0
        def get_valid_substring(i, sub_strings):
            nonlocal ans
            if i == len(s):
                ans = max(ans, len(sub_strings))
                return

            for j in range(i+1, len(s)+1):
                if s[i:j] in sub_strings:
                    continue
                sub_strings.add(s[i:j])
                get_valid_substring(j, sub_strings)
                sub_strings.remove(s[i:j])
        get_valid_substring(0, set())
        return ans