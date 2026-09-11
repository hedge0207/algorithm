class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum, even_sum = 0, 0
        for i in range(1, n*2+1):
            if i % 2 == 0:
                even_sum += i
            else:
                odd_sum += i

        while even_sum % odd_sum != 0:
            even_sum, odd_sum = odd_sum, even_sum % odd_sum
        return odd_sum