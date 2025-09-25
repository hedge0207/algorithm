class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        max_val = 0

        def backtrack(d, sub_or):
            nonlocal ans, max_val

            if d == n:
                if sub_or > max_val:
                    ans = 1
                    max_val = sub_or
                elif sub_or == max_val:
                    ans += 1
                return

            backtrack(d+1, sub_or | nums[d] if sub_or != 0 else nums[d])
            backtrack(d+1, sub_or)

        backtrack(0, 0)
        return ans








s = Solution()
print(s.countMaxOrSubsets([3,1]))
print(s.countMaxOrSubsets([2,2,2]))
print(s.countMaxOrSubsets([3,2,1,5]))





