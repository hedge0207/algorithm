import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        ans = len(heights)-1
        using_ladders = []
        for i in range(len(heights)-1):
            if heights[i+1] <= heights[i]:
                continue
            diff = heights[i+1] - heights[i]
            if ladders and len(using_ladders) == ladders:
                min_diff = heapq.heappop(using_ladders)
                if min_diff < diff and bricks - min_diff >= 0:
                    bricks -= min_diff
                else:
                    heapq.heappush(using_ladders, min_diff)
            if len(using_ladders) < ladders:
                heapq.heappush(using_ladders, diff)
            else:
                bricks -= diff
                if bricks < 0:
                    ans = i
                    break
        return ans