class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = 0
        suffix_sum = 0
        for i in range(1, n+1):
            suffix_sum += i

        for i in range(1, n+1):
            prefix_sum += i
            if prefix_sum == suffix_sum:
                return i
            suffix_sum -= i
        return -1