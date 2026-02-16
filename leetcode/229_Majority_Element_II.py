from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        ratio = len(nums) / 3
        ans = []
        for num, cnt in count.items():
            if cnt > ratio:
                ans.append(num)
        return ans