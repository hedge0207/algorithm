class Solution:
    def get_prime_list(self, n: int):
        sieve = [True] * n

        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i]:
                for j in range(i + i, n, i):
                    sieve[j] = False

        return [i for i in range(2, n) if sieve[i] == True]

    def closestPrimes(self, left: int, right: int) -> list[int]:
        prime_list = self.get_prime_list(right+1)
        ans = [-1, -1]
        min_diff = float("inf")
        for i in range(len(prime_list)-1):
            if left > prime_list[i]:
                continue

            if prime_list[i+1] - prime_list[i] < min_diff:
                ans = [prime_list[i], prime_list[i+1]]
                min_diff = prime_list[i+1] - prime_list[i]
        return ans