import heapq


def cookies(k, A):
    heapq.heapify(A)
    ans = 0
    while 1:
        least_sweetness = heapq.heappop(A)
        if least_sweetness >= k:
            break
        if len(A) == 0:
            return -1
        second_least_sweet = heapq.heappop(A)
        heapq.heappush(A, least_sweetness + second_least_sweet * 2)
        ans += 1
    return ans