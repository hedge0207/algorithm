class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        pos_num = 1
        for num in nums:
            if num <= 0:
                continue
            if num != pos_num:
                break
            pos_num += 1
        return pos_num