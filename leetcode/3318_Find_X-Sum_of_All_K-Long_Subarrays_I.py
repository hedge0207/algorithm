from collections import defaultdict
import heapq

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        count = defaultdict(int)
        ans = []
        for i in range(len(nums)):
            count[nums[i]] += 1
            if i >= k:
                count[nums[i-k]] -= 1

            if i >= k - 1:
                heap = []
                for num, cnt in count.items():
                    heapq.heappush(heap, (-cnt, -num))
                x_sum = 0
                for j in range(x):
                    if len(heap) == 0:
                        break
                    num, cnt = heapq.heappop(heap)
                    x_sum += num * cnt
                ans.append(x_sum)

        return ans