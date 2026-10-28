class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = {}
        ans = 0
        st = 0
        for ed in range(len(s)):
            char = s[ed]
            if cnt.get(char):
                cnt[char] += 1
            else:
                cnt[char] = 1
            while cnt[char] > 2:
                pre_char = s[st]
                cnt[pre_char] -= 1
                st += 1
            ans = max(ans, ed-st+1)
        return ans