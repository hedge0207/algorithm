class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        ans = 0
        for i in range(len(nums)-1):
            num = nums[i]
            left_sum += num
            right_sum -= num
            if (left_sum - right_sum) % 2 == 0:
                ans += 1
        return ans