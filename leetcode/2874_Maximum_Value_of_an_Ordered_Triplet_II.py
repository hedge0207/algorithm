class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        max_value_from_left = [0] * len(nums)
        max_value_from_left[0] = nums[0]
        max_value_from_right = [0] * len(nums)
        max_value_from_right[-1] = nums[-1]

        for i in range(1, len(nums)):
            max_value_from_left[i] = max(max_value_from_left[i-1], nums[i])

        for i in range(len(nums)-2, -1, -1):
            max_value_from_right[i] = max(max_value_from_right[i+1], nums[i])

        result = 0
        for j in range(1, len(nums)-1):
            result = max(result, (max_value_from_left[j-1] - nums[j]) * max_value_from_right[j+1])

        return result


# best_practice
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res
