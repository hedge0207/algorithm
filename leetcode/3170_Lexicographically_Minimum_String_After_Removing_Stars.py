import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        priority_queue = []
        removed = [0]*len(s)
        for i in range(len(s)):
            if s[i] == "*":
                removed[i] = 1
                if priority_queue:
                    _, idx = heapq.heappop(priority_queue)
                    removed[idx] = 1
            else:
                heapq.heappush(priority_queue, ([ord(s[i]), -i], i))

        ans = ""
        for char, is_removed in zip(s, removed):
            if not is_removed:
                ans += char
        return ans