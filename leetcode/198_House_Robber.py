# tabulation
class Solution:
    def rob(self, nums: list[int]) -> int:
        table = [0]*(len(nums)+2)

        for i in range(2, len(table)):
            table[i] = max(table[i-2]+nums[i-2], table[i-1])

        return table[-1]

# memoization
class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        def recur(d):
            if d < 0:
                return 0

            if memo.get(d) is not None:
                return memo[d]

            if d == 0:
                memo[0] = nums[0]
                return memo[0]

            memo[d] = max(recur(d-1), nums[d] + recur(d-2))
            return memo[d]

        recur(len(nums)-1)
        return memo[len(nums)-1]