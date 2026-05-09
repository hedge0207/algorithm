class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bits = []
        while n != 0:
            bits.append(1 if n % 2==0 else 0)
            n //= 2
        return sum(2**i*bits[i] for i in range(len(bits)))