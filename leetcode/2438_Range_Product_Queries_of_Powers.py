class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        powers = []
        for i, bit in enumerate(str(bin(n))[::-1]):
            if bit == "1":
                powers.append(2**i)

        ans = []
        for st, ed in queries:
            product = 1
            for i in range(st, ed+1):
                product *= powers[i]
            ans.append(product % (10**9+7))
        return ans