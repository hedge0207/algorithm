class Solution:
    def maximum69Number(self, num: int) -> int:
        ans = ""
        flag = True
        for digit in str(num):
            if flag and digit == "6":
                flag = False
                ans += "9"
            else:
                ans += digit
        return int(ans)