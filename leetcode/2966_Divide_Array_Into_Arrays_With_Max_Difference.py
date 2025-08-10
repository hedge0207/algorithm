class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        ans = []
        sub_arr = []
        for i in range(len(nums)):
            if len(sub_arr) == 0 or nums[i] - sub_arr[0] <= k:
                sub_arr.append(nums[i])
            else:
                return []
            if (i+1) % 3 == 0:
                ans.append(sub_arr)
                sub_arr = []
        return ans