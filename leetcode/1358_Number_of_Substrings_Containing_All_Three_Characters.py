class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = {"a": 0, "b": 0, "c": 0}
        ans = 0
        st = 0
        for ed in range(n):
            cnt[s[ed]] += 1
            while all(cnt.values()):
                cnt[s[st]] -= 1
                st += 1
                ans += n - ed
        return ans