import heapq

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        pri_queue = []
        for i in range(len(nums)):
            heapq.heappush(pri_queue, [nums[i], i])

        for i in range(k):
            num, idx = heapq.heappop(pri_queue)
            heapq.heappush(pri_queue, [num*multiplier, idx])

        ans = [0] * len(nums)
        while pri_queue:
            num, idx = heapq.heappop(pri_queue)
            ans[idx] = num
        return ans
