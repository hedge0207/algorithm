from collections import defaultdict

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            count[num-1] += 1

        ans = 0
        for num, cnt in count.items():
            if num-1 in count:
                ans = max(ans, cnt+count[num-1])

        return ans