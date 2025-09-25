class Solution:
    def maxSum(self, nums: list[int]) -> int:
        ans = nums[0]
        sum_ = nums[0]
        unique_nums = set([nums[0]])
        for i in range(1, len(nums)):
            num = nums[i]
            if num in unique_nums:
                continue
            if num < 0 and num < sum_:
                continue

            if sum_ < 0 and num > sum_:
                ans = max(ans, sum_)
                sum_ = num
                unique_nums = set()
            else:
                sum_ += num
            unique_nums.add(num)
            ans = max(ans, sum_)
        return ans