class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_cnt = 0
        for char in s:
            if char == "a":
                a_cnt += 1

        ans = a_cntas
        b_cnt = 0
        for char in s:
            if char == "b":
                b_cnt += 1
            else:
                a_cnt -= 1
            ans = min(ans, a_cnt + b_cnt)
        return ans