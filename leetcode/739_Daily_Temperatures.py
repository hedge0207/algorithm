from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        queue = deque([])
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while queue and temperatures[queue[-1]] < temperatures[i]:
                past_idx = queue.pop()
                result[past_idx] = i - past_idx
            queue.append(i)
        return result