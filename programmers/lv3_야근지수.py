import heapq


def solution(n, works):
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, -work)
    for i in range(n):
        work = heapq.heappop(max_heap)
        if work < 0:
            work += 1
        heapq.heappush(max_heap, work)

    answer = 0
    for work in max_heap:
        answer += work**2

    return answer