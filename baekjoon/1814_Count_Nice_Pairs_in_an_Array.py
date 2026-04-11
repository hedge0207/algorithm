from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        indices_per_rev = defaultdict(list)
        for i in range(len(nums)):
            indices_per_rev[nums[i]-int(str(nums[i])[::-1])].append(i)

        ans = 0
        for indices in indices_per_rev.values():
            ans += (len(indices) * (len(indices)-1)) // 2
        return ans % (10**9 + 7)