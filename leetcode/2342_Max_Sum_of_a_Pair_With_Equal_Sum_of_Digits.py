from collections import defaultdict


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        idx_per_sum = defaultdict(list)
        for num in nums:
            sum_ = 0
            for digit in str(num):
                sum_ += int(digit)
            if len(idx_per_sum[sum_]) >= 2:
                if min(idx_per_sum[sum_]) < num:
                    print(idx_per_sum, num)
                    idx_per_sum[sum_].remove(min(idx_per_sum[sum_]))
                    idx_per_sum[sum_].append(num)
                continue

            idx_per_sum[sum_].append(num)

        result = -1
        for digits in idx_per_sum.values():
            if len(digits) < 2:
                continue
            result = max(result, sum(digits))

        return result