from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None

        if (n := len(nums)) == 1:
            return nums[0]

        half = n // 2
        a = self.majorityElement(nums[half:])
        b = self.majorityElement(nums[:half])

        return [a, b][nums.count(b) > half]


s = Solution()
s.majorityElement([1, 2, 1, 2, 1, 2, 1, 2])
