class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        a_cnt = 0
        b_cnt = 0
        flag = False
        for i in range(len(s)):
            if i > 0 and s[i] != s[i-1]:
                if flag:
                    a_cnt = 0
                else:
                    b_cnt = 0
                flag = not flag
            if flag:
                if a_cnt > 0:
                    ans += 1
                    a_cnt -= 1
                b_cnt += 1
            else:
                if b_cnt > 0:
                    ans += 1
                    b_cnt -= 1
                a_cnt += 1
        return ans