import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        cap_pro = sorted([[cap, pro] for cap, pro in zip(capital, profits)])
        pri_queue = []
        for i in range(len(cap_pro)):
            cap, pro = cap_pro[i]
            while pri_queue and w < cap and k > 0:
                k -= 1
                w += -heapq.heappop(pri_queue)
            if w < cap:
                break
            heapq.heappush(pri_queue, -pro)

        for i in range(k):
            if len(pri_queue) == 0:
                break
            w += -heapq.heappop(pri_queue)
        return w