from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def custom_sort(a, b):
            if int(a+b) > int(b+a):
                return -1
            else:
                return 1
        nums = sorted(list(map(str, nums)), key=cmp_to_key(custom_sort), reverse=False)
        if nums[0] == "0":
            return "0"
        return "".join(nums)