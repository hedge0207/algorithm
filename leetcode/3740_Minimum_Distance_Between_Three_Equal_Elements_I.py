from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        indices_per_num = defaultdict(list)
        for i in range(len(nums)):
            indices_per_num[nums[i]].append(i)

        ans = -1
        for indices in indices_per_num.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices)-2):
                diff = 0
                diff += abs(indices[i] - indices[i+1])
                diff += abs(indices[i] - indices[i+2])
                diff += abs(indices[i+1] - indices[i+2])
                if ans == -1:
                    ans = diff
                else:
                    ans = min(ans, diff)
        return ans