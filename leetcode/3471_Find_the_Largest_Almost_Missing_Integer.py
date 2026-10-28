class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        if k > 1:
            st = nums[0]
            ed = nums[-1]
            if st == ed:
                return -1
            for i in range(1, len(nums)-1):
                if nums[i] == st:
                    st = -1
                if nums[i] == ed:
                    ed = -1
            return max(st, ed)
        else:
            count = {}
            for num in nums:
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1

            ans = -1
            for digit, num in count.items():
                if num != 1:
                    continue
                else:
                    ans = max(ans, digit)
            return ans