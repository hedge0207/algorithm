class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        pos, neg = [], []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        pos.sort(reverse=True)
        neg.sort()
        ans = None
        if len(neg) >= 2 and len(pos) >= 1:
            ans = neg[0] * neg[1] * pos[0]

        if len(pos) > 2:
            if ans is None:
                ans = 0
            ans = max(ans, pos[0] * pos[1] * pos[2])

        if ans is None:
            return neg[-1] * neg[-2] * neg[-3]
        return ans


# best_practice
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])