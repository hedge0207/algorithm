class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        first = second = float("inf")

        for x in nums[1:]:
            if x < first:
                second = first
                first = x
            elif x < second:
                second = x

        return nums[0] + first + second