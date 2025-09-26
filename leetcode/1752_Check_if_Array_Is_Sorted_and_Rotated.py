class Solution:
    def check(self, nums: list[int]) -> bool:
        post = nums[0]
        cnt = 0
        for i in range(1, len(nums)+1):
            i = i % len(nums)
            if nums[i] < post:
                cnt += 1
            post = nums[i]
        return False if cnt > 1 else True



s = Solution()
print(s.check([3, 4, 5, 1, 2]))