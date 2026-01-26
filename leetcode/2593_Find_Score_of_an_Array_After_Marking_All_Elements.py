class Solution:
    def findScore(self, nums: list[int]) -> int:
        nums_with_orig_idx = [[i, num] for i, num in enumerate(nums)]
        nums_with_orig_idx.sort(key=lambda x:(x[1], x[0]))
        marked = [0] * len(nums)
        ans = 0
        for idx, num in nums_with_orig_idx:
            if marked[idx]:
                continue
            ans += num
            left, right = idx-1, idx+1
            marked[idx] = 1
            if left >= 0:
                marked[left] = 1
            if right < len(nums):
                marked[right] = 1
        return ans