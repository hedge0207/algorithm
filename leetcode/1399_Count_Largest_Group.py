from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        max_len = 0
        group_per_sum = defaultdict(list)
        for i in range(1, n+1):
            sum_ = sum(map(int, str(i)))
            group_per_sum[sum_].append(i)
            max_len = max(max_len, len(group_per_sum[sum_]))

        ans = 0
        for nums in group_per_sum.values():
            if len(nums) == max_len:
                ans += 1

        return ans