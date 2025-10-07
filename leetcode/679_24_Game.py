class Solution:
    def judgePoint24(self, nums):
        if len(nums) == 1 and abs(nums[0] - 24) <= 0.001:
            return True
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    base = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    if self.judgePoint24(base + [nums[i] + nums[j]]):
                        return True
                    if self.judgePoint24(base + [nums[i] * nums[j]]):
                        return True
                    if self.judgePoint24(base + [nums[i] - nums[j]]):
                        return True
                    if self.judgePoint24(base + [nums[j] - nums[i]]):
                        return True
                    if nums[j] != 0 and self.judgePoint24(base + [nums[i] / nums[j]]):
                        return True
                    if nums[i] != 0 and self.judgePoint24(base + [nums[j] / nums[i]]):
                        return True
        return False
