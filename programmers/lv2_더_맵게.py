import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        min_score = heapq.heappop(scoville)
        if min_score >= k:
            break
        if len(scoville) == 0:
            answer = -1
            break
        second_min_score = heapq.heappop(scoville)
        heapq.heappush(scoville, min_score + second_min_score * 2)
        answer += 1

    return answer