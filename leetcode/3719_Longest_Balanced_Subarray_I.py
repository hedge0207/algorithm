class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            num_odd = 1 if nums[i] % 2 else 0
            num_even = 0 if nums[i] % 2 else 1
            distinct_nums = {nums[i]}
            for j in range(i+1, len(nums)):
                if nums[j] not in distinct_nums:
                    if nums[j] % 2 == 1:
                        num_odd += 1
                    else:
                        num_even += 1
                distinct_nums.add(nums[j])
                if num_odd == num_even:
                    ans = max(ans, j-i+1)
        return ans