class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                cnt += 1
                if cnt >= 3:
                    continue
            else:
                cnt = 1
            ans += s[i]
        return ans
