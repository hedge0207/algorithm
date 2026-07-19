class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (limit * 2 + 2)
        for i in range(n//2):
            a, b = nums[i], nums[n-i-1]
            l, h = min(a, b), max(a, b)

            diff[l+1] -= 1
            diff[h+limit+1] += 1
            diff[l+h] -= 1
            diff[l+h+1] += 1

        ans = float('inf')
        cur = n
        for i in range(2, 2 * limit + 1):
            cur += diff[i]
            ans = min(ans, cur)
        return ans