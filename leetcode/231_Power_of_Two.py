class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        while num <= n:
            if num == n:
                return True
            num *= 2

        return False