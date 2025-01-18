class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        set_a = set()
        set_b = set()
        n = len(A)
        result = [0] * n
        for i in range(n):
            set_a.add(A[i])
            set_b.add(B[i])
            result[i] = len(set_a & set_b)
        return result