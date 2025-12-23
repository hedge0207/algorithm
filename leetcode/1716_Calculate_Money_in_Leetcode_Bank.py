class Solution:
    def totalMoney(self, n: int) -> int:
        days = 0
        seed = 0
        i = 0
        ans = 0
        while days < n:
            if days % 7 == 0:
                seed += 1
                i = 0
            ans += seed + i
            i += 1
            days += 1
        return ans