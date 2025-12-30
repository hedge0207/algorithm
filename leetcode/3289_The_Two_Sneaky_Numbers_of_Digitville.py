class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        num_set = set()
        ans = []
        for num in nums:
            if num in num_set:
                ans.append(num)
            else:
                num_set.add(num)
        return ans