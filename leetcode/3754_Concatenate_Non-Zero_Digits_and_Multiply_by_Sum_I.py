class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zero_digits = ""
        sum_ = 0
        for digit in str(n):
            if digit != "0":
                non_zero_digits += digit
                sum_ += int(digit)
        if sum_ == 0:
            return 0
        return sum_ * int(non_zero_digits)