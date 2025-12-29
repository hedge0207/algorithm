import heapq

class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        post_color = colors[0]
        cnt = 1
        times = []
        heapq.heappush(times, neededTime[0])
        ans = 0
        for i in range(1, len(colors)):
            if colors[i] == post_color:
                cnt += 1
            else:
                if cnt > 1:
                    for _ in range(cnt-1):
                        ans += heapq.heappop(times)
                cnt = 1
                times = []
            heapq.heappush(times, neededTime[i])
            post_color = colors[i]
        if cnt > 1:
            for _ in range(cnt-1):
                ans += heapq.heappop(times)
        return ans




# best practice
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        time = 0
        prev = 0

        for i in range(1,len(colors)):
            if colors[i] == colors[prev]:
                if neededTime[i] < neededTime[prev]:
                    time += neededTime[i]
                else:
                    time += neededTime[prev]
                    prev = i

            else:
                prev = i

        return time