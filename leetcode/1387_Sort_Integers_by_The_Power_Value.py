from collections import defaultdict


class Solution:
    # memoization 없이
    def getKth(self, lo: int, hi: int, k: int) -> int:
        result = []
        for num in range(lo, hi + 1):
            power = 0
            new_num = num
            while new_num != 1:
                if new_num % 2:
                    new_num = 3 * new_num + 1
                else:
                    new_num //= 2
                power += 1
            result.append([power, num])
        result.sort(key=lambda x: (x[0], x[1]))
        return result[k - 1][1]

    # memoization 사용
    def get_kth_with_memoization(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}

        def power(x):
            if x in memo:
                return memo[x]
            memo[x] = 1 + power(3 * x + 1 if x % 2 else x // 2)
            return memo[x]

        result = [[power(x), x] for x in range(lo, hi + 1)]
        result = sorted(result, key=lambda x: (x[0], x[1]))
        return result[k - 1][1]


s = Solution()
s.get_kth_with_memoization(lo=12, hi=15, k=2)
