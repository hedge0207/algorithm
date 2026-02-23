class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        num = complexity[0]
        all_decrypted = True
        for i in range(1, len(complexity)):
            if complexity[i] <= num:
                all_decrypted = False
                break
        ans = 0
        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n-1)

        if all_decrypted:
            ans = factorial(len(complexity)-1)
        return ans % (10**9+7)