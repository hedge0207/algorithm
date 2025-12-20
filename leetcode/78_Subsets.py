class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def backtrack(d, arr):
            if d == len(nums):
                ans.append(arr)
                return

            backtrack(d+1, arr+[nums[d]])
            backtrack(d+1, arr)
        backtrack(0, [])
        return ans



s = Solution()
print(s.subsets([1,2,3]))