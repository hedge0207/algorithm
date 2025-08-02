class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        min_nums = []
        min_ = float("inf")
        for i in range(len(nums)):
            min_nums.append(min_)
            if min_ > nums[i]:
                min_ = nums[i]

        ans = -1
        for min_num, num in zip(min_nums, nums):
            diff = num-min_num
            if diff == 0:
                continue
            ans = max(num-min_num, ans)
        return ans
