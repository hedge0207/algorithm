class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10 ** 9 + 7
        m = len(s)

        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefix = [[0, 0]]
        sum_digits = [0]
        digits = 0
        sum_ = 0
        length = 0
        for char in s:
            if char != "0":
                length += 1
                digits = (digits * 10 + int(char)) % MOD
                sum_ += int(char)
                sum_ = sum_ % MOD
            prefix.append([digits, length])
            sum_digits.append(sum_)

        ans = []
        for st, ed in queries:
            ed += 1
            k = prefix[ed][1] - prefix[st][1]
            sub_string = (prefix[ed][0] - prefix[st][0] * pow10[k]) % MOD
            ans.append(sub_string * (sum_digits[ed] - sum_digits[st]) % MOD)
        return ans