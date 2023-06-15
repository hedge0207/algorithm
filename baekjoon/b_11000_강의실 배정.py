import sys
import heapq


input = sys.stdin.readline
N = int(input())

lectures = sorted([list(map(int, input().split())) for _ in range(N)])

lecture_queue = []
heapq.heappush(lecture_queue, lectures[0][1])

for i in range(1, N):
    if lectures[i][0] < lecture_queue[0]:
        heapq.heappush(lecture_queue, lectures[i][1])
    else:
        heapq.heappop(lecture_queue)
        heapq.heappush(lecture_queue, lectures[i][1])

print(len(lecture_queue))
