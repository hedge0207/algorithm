class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        ans = 0
        for word in words:
            if word[:len(pref)] == pref:
                ans += 1
        return ans


























s = Solution()
print(s.prefixCount(["pay","attention","practice","attend"], "at"))
print(s.prefixCount(["leetcode","win","loops","success"], "code"))