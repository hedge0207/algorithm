import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        priority_queue = []
        for p, t in classes:
            val = ((p+1)/(t+1)) - (p/t)
            heapq.heappush(priority_queue, [-val, p, t])

        for i in range(extraStudents):
            _, p, t = heapq.heappop(priority_queue)
            p += 1
            t += 1
            val = ((p + 1) / (t + 1)) - (p / t)
            heapq.heappush(priority_queue, [-val, p, t])
        sum_ = 0
        for _, p, t in priority_queue:
            sum_ += p / t
        return sum_ / len(classes)