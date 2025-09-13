import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()
        ans = 0
        day = 0
        i = 0
        min_heap = []

        while min_heap or i < len(events):
            if not min_heap:
                day = events[i][0]

            while i < len(events) and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            heapq.heappop(min_heap)
            ans += 1
            day += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
        return ans