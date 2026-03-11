class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ed = num
            st = 1
            divisors = set()
            while st < ed and len(divisors) <= 4:
                if num % st == 0:
                    divisors.add(st)
                    divisors.add(num // st)
                ed = num // st
                st += 1
            else:
                if len(divisors) == 4:
                    ans += sum(divisors)
        return ans